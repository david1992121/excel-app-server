from account.models import User
from account.serializers import BulkUploadSerializer, EmailRegisterSerializer, UserSerializer
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
import datetime

# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = EmailRegisterSerializer(data=request.data)
    if serializer.is_valid():
        input_data = serializer.validated_data
        email = input_data.get('email').strip()
        username = input_data.get('username').strip()
        password = input_data.get('password')

        if User.objects.filter(email__iexact=email).count() > 0:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            user = User.objects.create(email=email, username=username)
            user.set_password(password)
            user.save()
            return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(
                user=serializer.validated_data['user'])

            if not created:
                # update the created time of the token to keep it valid
                token.created = datetime.datetime.utcnow()
                token.save()

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_info(request):
    return Response(UserSerializer(request.user).data)


@api_view(['POST'])
@permission_classes([AllowAny])
def bulk_create(request):
    serializer = BulkUploadSerializer(data=request.data)
    if serializer.is_valid():
        input_data = serializer.validated_data
        code = input_data.get('code', '')
        if code == settings.UPLOAD_TOKEN:
            data = input_data.get('data', None)
            err_emails = []
            if data:
                for item in data:
                    try:
                        user = User(
                            email=item['email'],
                            username=item['username'])
                        user.set_password(item['pwd'])
                        user.save()
                    except Exception as e:
                        print(e)
                        err_emails.append(item['email'])
                if len(err_emails) == 0:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(
                        err_emails, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("heheeer", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

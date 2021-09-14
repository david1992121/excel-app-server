from ratio.serializers import RatioSerializer
from ratio.models import Ratio
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_list(request):
    ratio = Ratio.objects.filter(is_active = True).first()
    if ratio:
        return Response(RatioSerializer(ratio).data)
    else:
        return Response([])

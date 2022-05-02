from work.serializers import IndustrySerializer, RatioSerializer, SheetSerializer
from work.models import Industry, Ratio, Sheet
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, BasePermission


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_superuser:
            if request.user == obj.user:
                return True
            return False
        else:
            return True


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ratio_list(request):
    ratio = Ratio.objects.filter(is_active=True).first()
    if ratio:
        return Response(RatioSerializer(ratio).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_industry_list(request):
    industries = Industry.objects.order_by("order", "id").all()
    return Response(IndustrySerializer(industries, many=True).data)


class SheetsView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer

    def get_queryset(self):
        return self.queryset.filter(
            user_id=self.request.user.id).order_by('-created_at')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SheetsDetailView(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer

    def get_permissions(self):
        if self.request.method in ["GET", "PUT", "DELETE"]:
            self.permission_classes = [IsOwnerPermission]
        else:
            self.permission_classes = [IsAuthenticated]

        return super(SheetsDetailView, self).get_permissions()
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def check_sheet_title(request):
    sheet_id = request.query_params.get("id", "")
    title = request.query_params.get("title", "")
    if sheet_id != "" and title != "":
        sheet_id = int(sheet_id)
        if sheet_id > 0:
            try:
                sheet = Sheet.objects.get(pk=sheet_id)
                if sheet.user_id != request.user.id:
                    return Response(status=status.HTTP_403_FORBIDDEN)
            except Sheet.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(
            Sheet.objects.exclude(
                id=sheet_id).filter(
                user=request.user,
                title=title).count() == 0)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

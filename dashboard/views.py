from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets

from rest_framework.response import Response

from .filters import ShoppingFilter
from .serializers import *


class AppProfile(APIView):

    def get(self, request):
        ser = UserProfileSerializer(request.user)
        return Response(ser.data)


# Lessons Page
class Shop(APIView):
    template_name = 'dashboard/shop.html'

    def get(self, request):
        category = Category.objects.all().order_by("parent__id")
        ser = ShoppingSearchSerializer(instance={'categories': category})
        return Response(ser.data)


class ShoppingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = ShoppingSerializer
    filterset_class = ShoppingFilter
    ordering_fields = ['created_at', 'amount']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ShoppingDetailSerializer
        return super(ShoppingViewSet, self).get_serializer_class()

    test_param = openapi.Parameter('status', openapi.IN_QUERY, description="ADDED or DELETED",
                                   type=openapi.TYPE_STRING)

    @action(methods=['get'], detail=True,
            url_path='favourite', url_name='favourite')
    @swagger_auto_schema(manual_parameters=[test_param])
    def favourite(self, request, pk):
        user = request.user
        status1 = request.GET.get('status')
        if (status1 == None):
            return Response(user.favourites.filter(id=pk).exists())
        try:
            if (status1 == 'ADDED'):
                user.favourites.add(pk)
            elif (status1 == 'DELETED'):
                user.favourites.remove(pk)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response()

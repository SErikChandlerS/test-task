from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from server.apps.main.api.v1.serializers.user_reg_serializer import UserRegisterSerializer
from server.apps.main.models import User
from django_filters.rest_framework import DjangoFilterBackend


class RegisterUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data=data)

    filter_backends =[
        DjangoFilterBackend,
    ]
    filterset_fields = ['sex', 'first_name', 'last_name']

from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer, UserFullSerializer
from .models import User


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserListAPIView(ListAPIView):
    serializer_class = UserFullSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserFullSerializer
        return UserSerializer
        
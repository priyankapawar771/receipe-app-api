from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Receipe, User
from .serializers import RecipeSerializer, UserSerializer

# Create your views here.
class ReceipeViewSet(viewsets.ModelViewSet):
        serializer_class = RecipeSerializer
        queryset = Receipe.objects.all()
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]

        def get_queryset(self):
                return self.queryset.filter(user = self.request.user).order_by('-id')

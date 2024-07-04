from rest_framework import serializers
from .models import Receipe, User

class RecipeSerializer(serializers.ModelSerializer):
        class Meta:
                model = Receipe


class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
from lib2to3.pgen2.pgen import generate_grammar
from django.shortcuts import render
from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

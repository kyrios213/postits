from django.contrib.auth import models
from django.shortcuts import render, redirect
from rest_framework import generics, status, mixins
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from .serializers import *
from .forms import LoginForm
from .models import *

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def LoginView(request):
    form = LoginForm
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('api:register')
        else:
            messages.info(request, 'Username OR password is incorrect') 
    context = {'form': form, }
    return render(request, 'api/login.html', context) 

@login_required(login_url='api:login')
def LogoutUser(request):
    logout(request)
    return redirect('frontend:home')


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request):
        posts = Post.objects.all()     
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostByCategoryView(generics.ListAPIView):
    serializer_class = PostSerializer
    lookup_field = 'category'
    lookup_url_kwarg = 'category'

    def get_queryset(self):
        posts = Post.objects.filter(category=self.kwargs['category']).all()
        return posts

    def get_object(self):
        return self.get_queryset()
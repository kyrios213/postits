from django.shortcuts import render

from api.models import Category, UserProfile, Post
from .forms import UserReqisterForm



def HomeView(request):
    objs = Category.objects.all()
    form = UserReqisterForm
    return render(request, 'frontend/home.html', {'objs': objs, 'form': form})

def Profile(request, id):
    if request.user.id == id:
        profile = UserProfile.objects.get(id=id)
        posts = Post.objects.filter(author=profile.user)
    else: 
        profile = None
        posts = None
    context = {
        'profile': profile,
        'posts': posts
    }
    return render(request, 'frontend/profile.html', context)
from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('posts/', PostListCreateView.as_view(), name='posts'),
    path('category/<str:category>/', PostByCategoryView.as_view(), name='post_by_category')
]
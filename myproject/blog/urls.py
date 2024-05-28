from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('post/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view())    
]

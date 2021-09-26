from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostReplyView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='forum-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/reply', PostReplyView.as_view(), name='post-reply'),
    path('analytics/', views.analytics, name='forum-analytics'),
]

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse
from .models import Post, Reply
from .forms import ReplyForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'Forum/Home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'Forum/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'files']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Your Post was successful.')
        return super().form_valid(form)
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'files']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostReplyView(LoginRequiredMixin, CreateView):
    model = Reply
    template_name = 'Forum/reply_form.html'
    context_object_name = 'posts'
    fields = ['author', 'content']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

def analytics(request):
    return render(request,'Forum/Analytics.html', {'title': 'Analytics'})




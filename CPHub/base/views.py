from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post, Comment
# Create your views here.

class PostList(ListView):
    model = Post
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')

class PostDelete(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')



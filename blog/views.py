from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
                                        CreateView, 
                                        UpdateView,
                                        )

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post-list.html'

# details view
class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'

# create view
class PostCreateView(CreateView):
    model = Post
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']

# update view
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post-update.html'
    fields = ['title', 'content']
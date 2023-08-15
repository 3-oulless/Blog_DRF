from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import CreateOrUpdatePostModel
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.decorators import api_view
from rest_framework.response import Response
#MVT
class PostList(LoginRequiredMixin,ListView):
    login_url = '/account/login/'
    model = Post
    template_name = 'Post/PostList.html'
    context_object_name = 'Posts'
    ordering = '-id'


class DetailPost(LoginRequiredMixin,DetailView):
    login_url = '/account/login/'
    model = Post
    template_name = 'Post/PostDetail.html'
    context_object_name = 'post'


class CreatePost(LoginRequiredMixin,CreateView):
    login_url = '/account/login/'
    model = Post
    template_name = 'Post/PostCreate.html'
    form_class = CreateOrUpdatePostModel
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePost(LoginRequiredMixin,UpdateView):
    login_url = '/account/login/'
    model = Post
    template_name = 'Post/PostCreate.html'
    form_class = CreateOrUpdatePostModel
    success_url = '/'


class DeletePost(LoginRequiredMixin,DeleteView):
    login_url = '/account/login/'
    model = Post
    success_url = '/'
    template_name = 'Post/PostDelete.html'

#END MVT

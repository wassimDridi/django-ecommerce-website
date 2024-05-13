from django.shortcuts import render
from .models import Post
from .forms import PostForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

class ListePosts(ListView):
    model = Post
    template_name = 'post/liste_posts.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = Post
    template_name = 'post/detail_post.html'
    context_object_name = 'post'

    
class CreerPost(LoginRequiredMixin , CreateView):
    model = Post
    template_name = 'post/creer_post.html'
    form_class = PostForm  
    success_url = reverse_lazy('liste_posts') 
    def form_valid(self, form): 
        form.instance.author = self.request.user
        self.object = form.save()
        return super().form_valid(form)

class ModifierPost(UpdateView):
    model = Post
    template_name = 'post/modifier_post.html'
    form_class = PostForm  
    success_url = reverse_lazy('liste_posts')  
class SupprimerPost(DeleteView):
    model = Post
    template_name = 'post/supprimer_post.html'
    success_url = reverse_lazy('liste_posts')  
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm

from insta2.models import Post

# Create your views here.
class TestView(TemplateView):
  template_name = "test.html"

class PostsView(ListView):
  model = Post
  template_name = "index.html"

class PostDetailView(DetailView):
  model = Post
  template_name = "post.html"

class PostCreateView(CreateView):
  model = Post
  template_name = "post_create.html"
  fields = ['message', 'quote', 'createDate']

class PostEditView(UpdateView):
  model = Post
  template_name = "post_edit.html"
  fields = ['message', 'quote', 'createDate']

class PostDeleteView(DeleteView):
  model = Post
  template_name = "post_delete.html"
  success_url = reverse_lazy("posts")

class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = 'signup.html'
  success_url = reverse_lazy("login")
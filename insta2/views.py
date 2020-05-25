from django.views.generic import TemplateView, ListView, DetailView

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
from insta2.models import Post
from rest_framework import generics
from api.serializers import PostSerializer
# Create your views here.

class PostAPIView(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

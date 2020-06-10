from insta2.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('message', 'quote', 'createDate', 'updateDate')
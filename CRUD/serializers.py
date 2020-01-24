# Crud/serializers.py
from rest_framework import serializers
from .models import Post


# We created a serializer class called PostSerializer
# which will use the Post model with fields being the id, title and message.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'message')

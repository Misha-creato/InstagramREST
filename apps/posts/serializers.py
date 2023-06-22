from rest_framework import serializers
from .models import Post, Photo, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    photos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['author', 'description']

        
class PhotoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Photo
        fields = ['photo', 'post']
        
        
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Like
        fields = ['user', 'post']
        
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Comment
        fields = ['user', 'post', 'comment']
        
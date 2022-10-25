from rest_framework import serializers
from .models import Post, Category, Comment, Like, PostView
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class CommentSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ("user","content","id")

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    post_views = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()
    comment_count=serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'category', 'publish_date', 'last_updated','author', 'status', 'slug', 'comments', 'likes','post_views',"comment_count")
    
    def create(self, validated_data):
        author = User.objects.get(username=self.context['request'].user)
        validated_data['author'] = author
        return Post.objects.create(**validated_data)
    
    def get_likes(self, obj):
        return Like.objects.filter(post=obj).count()

    def get_post_views(self, obj):
        return PostView.objects.filter(post=obj).count()
    
    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()
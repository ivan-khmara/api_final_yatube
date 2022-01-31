from django.shortcuts import get_object_or_404
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def create(self, validated_data):
        user = get_object_or_404(User, username=validated_data.get('user'))
        following = get_object_or_404(
            User, username=validated_data.get('following')
        )
        if user == following:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя"
            )
        if Follow.objects.filter(
            user=user, following=following
        ).exists():
            raise serializers.ValidationError(
                f"Вы уже подписаны на {following}"
            )
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        read_only_fields = ('post',)
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')

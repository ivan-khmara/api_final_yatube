from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Follow, Group, Post
from .permissions import ChangeMadeOwner
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = (ChangeMadeOwner,)

    def get_queryset(self):
        post_id = self.kwargs['id']
        post = get_object_or_404(Post, pk=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post_id = self.kwargs['id']
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (ChangeMadeOwner,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter,)

    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        queryset = Follow.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

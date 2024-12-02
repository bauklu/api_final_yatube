from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import serializers

from api.permissions import OwnerOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             PostSerializer, GroupSerializer)
from posts.models import Post, Follow, Group


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, OwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, OwnerOrReadOnly,
    )

    def get_post(self):
        post_id = self.kwargs.get("post_id")
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (
        permissions.IsAuthenticated, permissions.IsAuthenticatedOrReadOnly,
    )
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    search_fields = ('^following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following_username = self.request.data.get('following')
        if Follow.objects.filter(
            user=self.request.user,
            following__username=following_username).exists() or\
                following_username == self.request.user.username:
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя'
            )
        serializer.save(user=self.request.user)

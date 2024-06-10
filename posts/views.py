from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comments", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = [
        "comments_count",
        "likes_count",
        "likes__created_at",
    ]
    search_fields = [
        "owner__username",
        "title"
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comments", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")

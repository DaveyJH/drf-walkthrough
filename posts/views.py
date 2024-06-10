from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet,
    DjangoFilterBackend
)
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostFilter(FilterSet):
    profiles = [*Post.objects.all().order_by("owner")]
    profile_choices = [
        (prof.owner.id, prof.owner.username,)
        for prof in profiles
    ]
    followed_by = ChoiceFilter(
        label="Followed by",
        field_name="owner__followed__owner__profile",
        choices=profile_choices
    )
    liked_by = ChoiceFilter(
        label="Liked by",
        field_name="likes__owner__profile",
        choices=profile_choices
    )
    authored_by = ChoiceFilter(
        label="Authored by",
        field_name="owner__profile",
        choices=profile_choices
    )

    class Meta:
        fields = [
            "followed_by",
            "liked_by",
            "authored_by",
        ]
        model = Post


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comments", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    # filterset_fields = [
    #     "owner__followed__owner__profile",
    #     "likes__owner__profile",
    #     "owner__profile",
    # ]
    filterset_class = PostFilter
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

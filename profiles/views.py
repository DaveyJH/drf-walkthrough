from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet,
    DjangoFilterBackend
)
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileFollowerFilter(FilterSet):
    profiles = [*Profile.objects.all().order_by("owner")]
    choices = [(prof.owner.id, prof.owner.username,) for prof in profiles]
    following = ChoiceFilter(
        label="Following",
        field_name="owner__following__followed__profile",
        choices=choices
    )

    class Meta:
        fields = ["following",]
        model = Profile


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count("owner__post", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    # filterset_fields = [
    #     "owner__following__followed__profile",
    # ]
    filterset_class = ProfileFollowerFilter
    ordering_fields = [
        "posts_count",
        "followers_count",
        "following_count",
        "owner__followed__created_at",
        "owner__following__created_at",
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count("owner__post", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")

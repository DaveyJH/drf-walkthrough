from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Post
from profiles.models import Profile


class PostFilter(FilterSet):
    profiles = [*Profile.objects.all().order_by("owner")]
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

from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Post
from profiles.models import Profile


class PostFilter(FilterSet):
    followed_by = ChoiceFilter(
        label="Followed by",
        field_name="owner__followed__owner__profile",
        choices=[]
    )
    liked_by = ChoiceFilter(
        label="Liked by",
        field_name="likes__owner__profile",
        choices=[]
    )
    authored_by = ChoiceFilter(
        label="Authored by",
        field_name="owner__profile",
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        profiles = Profile.objects.all().order_by("owner")
        # Create choices dynamically
        filters = ["followed_by", "liked_by", "authored_by"]
        for filter in filters:
            self.filters[filter].extra['choices'] = [
                (
                    profile.owner.id,
                    profile.owner.username
                ) for profile in profiles
            ]

    class Meta:
        fields = [
            "followed_by",
            "liked_by",
            "authored_by",
        ]
        model = Post

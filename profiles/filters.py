from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Profile


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

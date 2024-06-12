from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Comment


class CommentFilter(FilterSet):
    comments = [*Comment.objects.all().order_by("owner")]
    choices = [(
        comment.post.id,
        comment.post.title,
        ) for comment in comments
    ]
    post = ChoiceFilter(
        label="Post",
        field_name="post",
        choices=choices
    )

from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Comment
from posts.models import Post


class CommentFilter(FilterSet):
    posts = [*Post.objects.all().order_by("owner")]
    choices = [(
        post.id,
        post.title,
        ) for post in posts
    ]
    post = ChoiceFilter(
        label="Post",
        field_name="post",
        choices=choices
    )

    class Meta:
        fields = [
            "post",
        ]
        model = Comment

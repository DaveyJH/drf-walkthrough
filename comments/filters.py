from django_filters.rest_framework import (
    ChoiceFilter,
    FilterSet
)
from .models import Comment
from posts.models import Post


class CommentFilter(FilterSet):
    post = ChoiceFilter(
        label="Post",
        field_name="post",
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        posts = Post.objects.all().order_by("owner")
        # Create choices dynamically
        self.filters['post'].extra['choices'] = [
            (post.id, post.title) for post in posts
        ]

    class Meta:
        fields = [
            "post",
        ]
        model = Comment

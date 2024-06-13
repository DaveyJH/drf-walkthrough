from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    time_of_last_update = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_time_of_last_update(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            "id",
            "owner",
            "post",
            "created_at",
            "updated_at",
            "time_of_last_update",
            "content",
            "is_owner",
            "profile_id",
            "profile_image",
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source="post.id")

"""lms_courseware serializer file."""
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.lms_courseware.models import Chapter, Course, SubChapter


class UserSerializer(serializers.ModelSerializer):
    """User serializer class.

    Parameters
    ----------
    serializers : rest_framework
    """

    class Meta:  # noqa: D106
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "password",
            "date_joined",
            "last_login",
        )
        read_only_fields = (
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "last_login",
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}


class CourseSerializer(serializers.ModelSerializer):
    """Course serializer class.

    Parameters
    ----------
    serializers : rest_framework
    """

    class Meta:  # noqa: D106
        model = Course
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    """Chapter serializer class.

    Parameters
    ----------
    serializers : rest_framework
    """

    class Meta:  # noqa: D106
        model = Chapter
        fields = "__all__"


class SubChapterSerializer(serializers.ModelSerializer):
    """Subchapter serializer class.

    Parameters
    ----------
    serializers : rest_framework
    """

    class Meta:  # noqa: D106
        model = SubChapter
        fields = "__all__"

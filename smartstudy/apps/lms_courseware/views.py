"""lms_courseware views file."""
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.lms_courseware.models import Chapter, Course, SubChapter
from apps.lms_courseware.serializers import (
    ChapterSerializer,
    CourseSerializer,
    SubChapterSerializer,
    UserSerializer,
)
from apps.pagination import StandardResultsSetPagination


class UserViewSet(viewsets.ModelViewSet):
    """User viewset class.

    This viewset automatically provides `list`, `create`, `modify` and `delete`
    actions.

    Parameters
    ----------
    viewsets : rest_framework

    """

    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination


class CourseViewSet(viewsets.ModelViewSet):
    """Course viewset class.

    This viewset automatically provides `list`, `create`, `modify` and `delete`
    actions.

    Parameters
    ----------
    viewsets : rest_framework

    """

    queryset = Course.objects.all().order_by("-id")
    serializer_class = CourseSerializer
    pagination_class = StandardResultsSetPagination


class ChapterViewSet(viewsets.ModelViewSet):
    """Chapter viewset class.

    This viewset automatically provides `list`, `create`, `modify` and `delete`
    actions.

    Parameters
    ----------
    viewsets : rest_framework

    """

    queryset = Chapter.objects.all().order_by("-id")
    serializer_class = ChapterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["course_id"]
    pagination_class = StandardResultsSetPagination


class SubChapterViewSet(viewsets.ModelViewSet):
    """Subchapter viewset class.

    This viewset automatically provides `list`, `create`, `modify` and `delete`
    actions.

    Parameters
    ----------
    viewsets : rest_framework

    """

    queryset = SubChapter.objects.all().order_by("-id")
    serializer_class = SubChapterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["chapter_id"]
    pagination_class = StandardResultsSetPagination

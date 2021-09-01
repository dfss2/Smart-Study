"""lms_courseware admin file."""
from django.contrib import admin

from apps.lms_courseware.models import (
    Chapter,
    Course,
    SubChapter,
    TextSubChapter,
    VideoSubChapter,
)


class CourseAdmin(admin.ModelAdmin):
    """Course model admin.

    Parameters
    ----------
    admin : django.contrib
    """

    list_display = ("id", "title")


admin.site.register(Course, CourseAdmin)


class ChapterAdmin(admin.ModelAdmin):
    """Chapter model admin.

    Parameters
    ----------
    admin : django.contrib
    """

    list_display = ("id", "title", "course")


admin.site.register(Chapter, ChapterAdmin)


class SubChapterAdmin(admin.ModelAdmin):
    """SubChapter model admin.

    Parameters
    ----------
    admin : django.contrib
    """

    list_display = ("id", "chapter")


admin.site.register(SubChapter, SubChapterAdmin)


class TextSubChapterAdmin(admin.ModelAdmin):
    """TextSubChapter model admin.

    Parameters
    ----------
    admin : django.contrib
    """

    list_display = ("id", "content")


admin.site.register(TextSubChapter, TextSubChapterAdmin)


class VideoSubChapterAdmin(admin.ModelAdmin):
    """VideoSubChapter model admin.

    Parameters
    ----------
    admin : django.contrib
    """

    list_display = ("id", "url")


admin.site.register(VideoSubChapter, VideoSubChapterAdmin)

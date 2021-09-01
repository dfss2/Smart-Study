"""lms_courseware models file."""
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Course(models.Model):
    """Course model class.

    Parameters
    ----------
    models : django.db
    """

    user = models.ManyToManyField(User, related_name="courses")
    title = models.CharField(_("title"), max_length=64)
    description = models.TextField(_("description"), blank=True)

    class Meta:  # noqa: D106
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self):
        """Str representation of course model.

        Returns
        -------
        str
            containing title of the course
        """
        return f"{self.title}"


class Chapter(models.Model):
    """Chapter model class.

    Parameters
    ----------
    models : django.db
    """

    title = models.CharField(_("title"), max_length=64)
    description = models.TextField(_("description"), blank=True)
    course = models.ForeignKey(
        Course, related_name="chapters", on_delete=models.CASCADE
    )

    class Meta:  # noqa: D106
        verbose_name = "chapter"
        verbose_name_plural = "chapters"

    def __str__(self):
        """Str representation of chapter model.

        Returns
        -------
        str
            containing title of the chapter
        """
        return f"{self.title}"


class SubChapter(models.Model):
    """Subchapter model class.

    Parameters
    ----------
    models : django.db
    """

    chapter = models.ForeignKey(
        Chapter, related_name="subchapters", on_delete=models.CASCADE
    )

    class Meta:  # noqa: D106
        verbose_name = "subchapter"
        verbose_name_plural = "subchapters"

    def __str__(self):
        """Str representation of subchapter model.

        Returns
        -------
        str
            containing id of the subchapter
        """
        return f"{self.id}"


class TextSubChapter(SubChapter):
    """TextSubChapter model class.

    Parameters
    ----------
    models : django.db
    """

    content = models.TextField(_("content"))

    class Meta:  # noqa: D106
        verbose_name = "textsubchapter"
        verbose_name_plural = "textsubchapters"

    def __str__(self):
        """Str representation of textsubchapter model.

        Returns
        -------
        str
            containing id of the textsubchapter
        """
        return f"{self.id}"


class VideoSubChapter(SubChapter):
    """VideoSubChapter model class.

    Parameters
    ----------
    models : django.db
    """

    url = models.URLField(_("url"), max_length=200)

    class Meta:  # noqa: D106
        verbose_name = "videosubchapter"
        verbose_name_plural = "videosubchapters"

    def __str__(self):
        """Str representation of videosubchapter model.

        Returns
        -------
        str
            containing id of the videosubchapter
        """
        return f"{self.id}"

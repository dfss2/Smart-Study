"""lms_courseware config file."""
from django.apps import AppConfig


class LmsCoursewareConfig(AppConfig):
    """API configuration class.

    Parameters
    ----------
    AppConfig : django.apps
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.lms_courseware"

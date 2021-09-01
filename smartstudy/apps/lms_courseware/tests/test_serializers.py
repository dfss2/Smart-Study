"""Serializers test cases."""
from django.contrib.auth.models import User
from django.test import TestCase

from apps.lms_courseware.models import Course
from apps.lms_courseware.serializers import CourseSerializer


class CourseSerializerTestCase(TestCase):
    """Course serializer test cases.

    Parameters
    ----------
    TestCase : django.test
    """

    def setUp(self):
        """Set up the data for each test case."""
        user = User.objects.create(
            username="john_doe",
            password="12345678",
            first_name="john",
            last_name="doe",
        )
        course = {
            "title": "Course 1",
            "description": "course-1",
        }

        course_obj = Course.objects.create(**course)
        user.courses.add(course_obj)

        self.serializer = CourseSerializer(instance=course_obj)

    def test_contains_expected_fields(self):
        """Test that serializer data contain expected model fields."""
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()), set(["id", "title", "description", "user"])
        )

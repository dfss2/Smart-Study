"""Views test cases."""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.lms_courseware.models import Course


class CourseViewSetTestCase(TestCase):
    """Course viewset test cases.

    Parameters
    ----------
    TestCase : django.test
    """

    def setUp(self):
        """Set up the database records for each test case."""
        self.user = User.objects.create(
            username="john_doe",
            password="12345678",
            first_name="john",
            last_name="doe",
        )
        self.courses = [
            {
                "title": "Course 1",
                "description": "course-1",
            },
            {
                "title": "Course 2",
                "description": "course-2",
            },
            {
                "title": "Course 3",
                "description": "course-3",
            },
            {
                "title": "Course 4",
                "description": "course-4",
            },
            {
                "title": "Course 5",
                "description": "course-5",
            },
        ]
        # insert data in the database
        for course in self.courses:
            c = Course.objects.create(**course)
            self.user.courses.add(c)

    def test_api_returns_all_records(self):
        """Test that url returns all courses from the db."""
        res = self.client.get(reverse("lms_courseware:courses-list"))
        self.assertEqual(res.json()["count"], len(self.courses))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_creates_course_in_db(self):
        """Test that api creates a new course in the db."""
        data = {
            "user": self.user.id,
            "title": "Test Course",
            "description": "test course",
        }
        res = self.client.post(
            reverse("lms_courseware:courses-list"), data=data
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        json_res = res.json()
        self.assertEqual(json_res["title"], "Test Course")
        self.assertEqual(json_res["description"], "test course")

    def test_api_updates_course_in_db(self):
        """Test that api updates a course with given course id in the db."""
        obj = {"title": "Updated Test Course"}
        data = Course.objects.values("id").first()
        res = self.client.patch(
            reverse(
                "lms_courseware:courses-detail", kwargs={"pk": data.get("id")}
            ),
            data=obj,
            content_type="application/json",
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        json_res = res.json()
        self.assertEqual(json_res["title"], "Updated Test Course")

    def test_api_with_given_course_id_deletes_data(self):
        """Test that api deletes data with given course id in the db."""
        data = Course.objects.values("id").first()
        res = self.client.delete(
            reverse(
                "lms_courseware:courses-detail", kwargs={"pk": data.get("id")}
            )
        )
        # assert that data is deleted from the db
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

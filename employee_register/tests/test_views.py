from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from employee_register.models import Employee, Position


class EmployeeViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")

        self.position = Position.objects.create(title="HR")
        Employee.objects.create(
            fullname="Test User",
            emp_code="001",
            mobile="01700000000",
            position=self.position,
        )

    def test_employee_list_page_loads(self):
        response = self.client.get(reverse("employee_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")

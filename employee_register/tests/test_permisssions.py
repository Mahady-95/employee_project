from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class EmployeePermissionTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_login_required_redirect(self):
        response = self.client.get(reverse("employee_list"))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_logged_in_user_can_access(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("employee_list"))
        self.assertEqual(response.status_code, 200)

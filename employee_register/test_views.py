from django.test import TestCase
from django.urls import reverse
from .models import Employee, Position

class EmployeeViewTest(TestCase):

    def test_employee_list_page_status(self):
        response = self.client.get(reverse("employee_list"))
        self.assertEqual(response.status_code, 302)

    # def setUp(self):
    #     self.position = Position.objects.create(title="Manager")

    # def test_employee_list_page_status(self):
    #     response = self.client.get(reverse("employee_list"))
    #     self.assertEqual(response.status_code, 200)

    def test_employee_create_page_loads(self):
        response = self.client.get(reverse("employee_list"))
        self.assertEqual(response.status_code, 302)
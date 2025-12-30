from django.test import TestCase
from django.urls import reverse

class EmployeeViewTest(TestCase):

    def test_employee_list_page_status(self):
        response = self.client.get(reverse("employee_list"))
        self.assertEqual(response.status_code, 200)
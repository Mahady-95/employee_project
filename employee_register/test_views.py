# from django.test import TestCase
# from django.urls import reverse

# class EmployeeViewTest(TestCase):

#     def test_employee_list_page_status(self):
#         response = self.client.get(reverse("employee_list"))
#         self.assertEqual(response.status_code, 200)

from django.urls import reverse
from django.test import TestCase
from employee_register.models import Employee

class EmployeeCreateTest(TestCase):
    def test_create_employee(self):
        response = self.client.post(reverse('employee_create'), {
            'fullname': 'Test User',
            'emp_code': 'EMP01',
            'mobile': '01700000000'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 1)

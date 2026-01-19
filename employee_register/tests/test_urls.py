from django.test import SimpleTestCase
from django.urls import reverse, resolve
from employee_register import views


class EmployeeURLTest(SimpleTestCase):

    def test_employee_list_url_resolves(self):
        url = reverse("employee_list")
        self.assertEqual(resolve(url).func, views.employee_list)

    def test_employee_insert_url_resolves(self):
        url = reverse("employee_insert")
        self.assertEqual(resolve(url).func, views.employee_form)

    def test_employee_update_url_resolves(self):
        # Use dummy id
        url = reverse("employee_update", args=[1])
        self.assertEqual(resolve(url).func, views.employee_form)

    def test_employee_delete_url_resolves(self):
        url = reverse("employee_delete", args=[1])
        self.assertEqual(resolve(url).func, views.employee_delete)

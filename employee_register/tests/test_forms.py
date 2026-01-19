from django.test import TestCase
from employee_register.forms import EmployeeForm
from employee_register.models import Position


class EmployeeFormTest(TestCase):

    def setUp(self):
        self.position = Position.objects.create(title="HR")

    def test_empty_fullname_invalid(self):
        form = EmployeeForm(
            data={
                "fullname": "",
                "emp_code": "123",
                "mobile": "01900000000",
                "position": self.position.id,
            }
        )
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form = EmployeeForm(
            data={
                "fullname": "Mahady",
                "emp_code": "123",
                "mobile": "01900000000",
                "position": self.position.id,
            }
        )
        self.assertTrue(form.is_valid())

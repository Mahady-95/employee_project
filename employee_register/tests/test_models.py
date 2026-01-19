from django.test import TestCase
from employee_register.models import Employee, Position


class EmployeeModelTest(TestCase):

    def setUp(self):
        self.position = Position.objects.create(title="HR")

    def test_employee_creation(self):
        emp = Employee.objects.create(
            fullname="Mahady",
            emp_code="707",
            mobile="01900000000",
            position=self.position,
        )
        self.assertEqual(emp.fullname, "Mahady")
        self.assertEqual(emp.position.title, "HR")
        self.assertEqual(str(emp), "Mahady")
        self.assertEqual(Employee.objects.count(), 1)

    def test_duplicate_emp_code_not_allowed(self):
        Employee.objects.create(
            fullname="Mahady",
            emp_code="707",
            mobile="01900000000",
            position=self.position,
        )
        with self.assertRaises(Exception):
            Employee.objects.create(
                fullname="Test",
                emp_code="707",
                mobile="01800000000",
                position=self.position,
            )

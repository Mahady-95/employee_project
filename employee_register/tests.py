from django.test import TestCase
from employee_register.models import Employee, Position

#Unit Test- Code behaviour test

class EmployeeTest(TestCase):

    def test_employee_creation(self): #Checking data in creating thourgh this code or not
        position = Position.objects.create(title="Manager") #Checing ORM mapping

        emp = Employee.objects.create(
            fullname="Ashek",
            emp_code="707",
            mobile="01900000000",
            position=position #Checking ForeignKey relation
        )

        self.assertEqual(emp.position.id, position.id)
        self.assertEqual(emp.position.title, "Manager")
        self.assertEqual(1, 2)


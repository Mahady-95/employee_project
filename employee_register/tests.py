from django.test import TestCase
from django.urls import reverse
from employee_register.models import Employee, Position

#Unit Test- Code behaviour test

class EmployeeTest(TestCase):


    # Create
    def setUp(self):
        self.position = Position.objects.create(title="Manager") #Checing ORM mapping

    def test_employee_creation(self):
        emp = Employee.objects.create(
            fullname="Chorki",
            emp_code="707",
            mobile="01900000000",
            position=self.position
        )

        self.assertEqual(emp.position.id, self.position.id)
        self.assertEqual(emp.position.title, "Manager")
    
    #Update
    def test_employee_update(self):
        emp = Employee.objects.create(
            fullname="Ashek",
            emp_code="707",
            mobile="01900000000",
            position=self.position
        )

        response = self.client.post(
            reverse("employee_update", args=[emp.id]),
            {
                "fullname": "Mahady",
                "emp_code": "002",
                "mobile": "01800000000",
                "position": self.position.id,
            }
        )

        emp.refresh_from_db()
        self.assertEqual(emp.fullname, "Mahady")

    # Delete
    def test_employee_delete(self):
        emp = Employee.objects.create(
            fullname="Mahady",
            emp_code="202",
            mobile="01800000000",
            position=self.position
        )

        response = self.client.post(
            reverse("employee_delete", args=[emp.id])
        )

        self.assertEqual(Employee.objects.count(), 0)





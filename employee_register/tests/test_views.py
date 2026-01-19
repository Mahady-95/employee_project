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

    # LIST PAGE
    def test_employee_list_page_loads(self):
        response = self.client.get(reverse("employee_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")
        self.assertTemplateUsed(response, "employee_register/employee_list.html")

    # CREATE
    def test_employee_create(self):
        response = self.client.post(
            reverse("employee_insert"),
            {  # <-- fixed
                "fullname": "Mahady",
                "emp_code": "002",
                "mobile": "01800000000",
                "position": self.position.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.filter(emp_code="002").count(), 1)

    # UPDATE
    def test_employee_update(self):
        emp = Employee.objects.first()
        response = self.client.post(
            reverse("employee_update", args=[emp.id]),
            {
                "fullname": "Mahady Updated",
                "emp_code": "001",
                "mobile": "01900000001",
                "position": self.position.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        emp.refresh_from_db()
        self.assertEqual(emp.fullname, "Mahady Updated")
        self.assertEqual(emp.mobile, "01900000001")

    # DELETE
    def test_employee_delete(self):
        emp = Employee.objects.first()
        response = self.client.post(reverse("employee_delete", args=[emp.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 0)

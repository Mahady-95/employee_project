from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from employee_register.models import Employee, Position


class EmployeeTest(TestCase):

    def setUp(self):
        # 🔐 Create & login user (REQUIRED for login_required views)
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")

        # 🔹 Create position
        self.position = Position.objects.create(title="HR")

    # ✅ CREATE
    def test_employee_creation(self):
        emp = Employee.objects.create(
            fullname="Mahady Ashek",
            emp_code="707",
            mobile="01900000000",
            position=self.position,
        )

        self.assertEqual(emp.position.id, self.position.id)
        self.assertEqual(emp.position.title, "HR")
        self.assertEqual(Employee.objects.count(), 1)

    # ✅ UPDATE
    def test_employee_update(self):
        emp = Employee.objects.create(
            fullname="Ashek",
            emp_code="707",
            mobile="01900000000",
            position=self.position,
        )

        response = self.client.post(
            reverse("employee_update", args=[emp.id]),
            {
                "fullname": "Mahady",
                "emp_code": "002",
                "mobile": "01800000000",
                "position": self.position.id,
            },
        )

        # 🔹 Ensure redirect after successful update
        self.assertEqual(response.status_code, 302)

        emp.refresh_from_db()
        self.assertEqual(emp.fullname, "Mahady")
        self.assertEqual(emp.emp_code, "002")
        self.assertEqual(emp.mobile, "01800000000")

    # ✅ DELETE
    def test_employee_delete(self):
        emp = Employee.objects.create(
            fullname="Mahady",
            emp_code="202",
            mobile="01800000000",
            position=self.position,
        )

        response = self.client.post(reverse("employee_delete", args=[emp.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 0)

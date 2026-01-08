from django import forms
from .models import Employee
import re

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'emp_code', 'mobile', 'position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP Code',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position"

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        if not re.match(r'^\d{10,15}$', mobile):
            raise forms.ValidationError("Enter a valid mobile number (10–15 digits).")

        return mobile

    def clean_emp_code(self):
        emp_code = self.cleaned_data.get('emp_code')

        if not emp_code:
            raise forms.ValidationError("Employee code is required.")

        if len(emp_code) > 3:
            raise forms.ValidationError("Employee code must be max 3 characters.")

        return emp_code.upper()

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee
import re

# ------------------------------
# Employee Form (CRUD)
# ------------------------------
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

        # Bootstrap 4 classes + placeholders
        self.fields['fullname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter full name'
        })
        self.fields['emp_code'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Max 3 characters'
        })
        self.fields['mobile'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter mobile number'
        })
        self.fields['position'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['position'].empty_label = "Select Position"

    # Fullname validation
    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if len(fullname) < 3:
            raise forms.ValidationError("Full name must be at least 3 characters.")
        return fullname.strip().title()

    # Mobile validation
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match(r'^\d{10,15}$', mobile):
            raise forms.ValidationError(
                "Enter a valid mobile number (10–15 digits)."
            )
        return mobile

    # Employee code validation
    def clean_emp_code(self):
        emp_code = self.cleaned_data.get('emp_code')
        if not emp_code:
            raise forms.ValidationError("Employee code is required.")
        if len(emp_code) > 3:
            raise forms.ValidationError("Employee code must be max 3 characters.")
        return emp_code.upper()


# ------------------------------
# Custom Login Form
# ------------------------------
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Bootstrap 4 class + placeholder
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })

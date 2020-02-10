from django import forms
from testApp.models import *


class LoginForm(forms.ModelForm):
    class Meta:

        model = company_profile
        exclude=[
            "role_id",
            "company_email",
            "company_password",
            "company_name",
            "mobile_number",
            "website_url",
            "password_updated",
            "is_active",
        ]


class hr_profileForm(forms.ModelForm):
    class Meta:
        model = hr_profile
        exclude = [
            "role_id",
            "hr_firstname",
            "hr_lastname",
            "hr_fullname",
            "hr_email",
            "hr_password",
            "hr_mobile",
            "is_active",
        ]

class change_passForm(forms.ModelForm):
    class Meta:
        model = company_profile
        exclude =[
            "company_userpassword",

        ]
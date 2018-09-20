from django import forms
from .models import Token
from .models import User


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = [
            'empName',
            'empId',
            'phone',
            'lunch',
            ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'firstName',
            'lastName',
            'email',
            'phone',
            'password',
            ]

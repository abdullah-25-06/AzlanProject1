from django import forms
from .models import Student
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator


class StudentForm(forms.ModelForm):
    name = forms.CharField(validators=[MinLengthValidator(3, 'Enter atleast 3 letter Name'),
                                       MaxLengthValidator(30, 'Name should be less than 30 letters')])
    fname = forms.CharField(validators=[MinLengthValidator(3, 'Enter atleast 3 letter Father Name'),
                                        MaxLengthValidator(30, 'Father Name should be less than 30 letters')])
    email = forms.EmailField(validators=[EmailValidator('Please enter a valid Email')])

    class Meta:
        model = Student
        fields = ['name', 'fname', 'email', 'seat', ]

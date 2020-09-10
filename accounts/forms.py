from django.contrib.auth.models import User
from django import forms

class RegisterFrom(forms.ModelForm):
    password=forms.CharField(label="PW",widget=forms.PasswordInput)
    password_check=forms.CharField(label="Repeat PW",widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


    def clean_password_check(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password_check']:
            raise forms.ValidationError("pw not matched")
        return cd['password_check']
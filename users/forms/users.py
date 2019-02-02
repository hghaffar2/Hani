from users.models.users import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



class UserForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid emailaddress.')
    gender = forms.CharField(widget=forms.RadioSelect(choices=User.GENDER_CHOICES))
    city = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=12,min_length=10)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','gender','phone', 'city', )

    def clean_email(self):

        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            return forms.ValidationError('this email is already existing')
        else:
            return email


    def clean_username(self):

        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            return forms.ValidationError('this username is already existing')
        else:
            return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


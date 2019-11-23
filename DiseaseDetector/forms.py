from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from DiseaseDetector.models import User


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'maxlength': 30,
        'placeholder': 'Username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise ValidationError("Sorry, that login or password is invalid. Please try again.")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
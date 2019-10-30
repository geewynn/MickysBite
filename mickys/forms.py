from django import forms
from django.contrib.auth.models import User
from mickys.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password')


class UserProfileForms(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile_number',)


class ProductForm(forms.ModelForm):
    class Meta:
        fields = '__all__'

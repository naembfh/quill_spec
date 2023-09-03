from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if  password1 != password2:
            # print('there')
            raise forms.ValidationError("Passwords do not match. Please enter matching passwords.")
        # print('here')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()  

        user_profile = User_profile(user=user)
        user_profile.save()  

        return user



class Edit_profile_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class User_Profile_Form(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ['phone_no', 'user_type']



  
   
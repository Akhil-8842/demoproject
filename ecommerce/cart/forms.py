from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gender_choice = [('male', "Male"), ('female', 'Female')]
    gender = forms.ChoiceField(
        choices=gender_choice,
        widget=forms.RadioSelect(attrs={'class': 'inline-radio'}),
        required=True
    )
    # gender_choice = [('male', "Male"), ('female', 'Female')]
    # gender = forms.ChoiceField(choices=gender_choice, widget=forms.RadioSelect, required=True)
    class Meta:
        model = User
        fields = ['username', 'email','gender', 'password1', 'password2']
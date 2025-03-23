from random import choice

from django.contrib.auth.forms import UserCreationForm

from app1.models import School
from django import forms


class Schoolform(forms.ModelForm):
    location_choices=[('Ernakulam','EKM'),('Trivandrum','TVM'),('Kollam','kollam')]
    location=forms.ChoiceField(choices= location_choices,widget=forms.Select,required=True)




    class Meta:
        model=School

        fields=['name','location','principal']
from django import forms
from .models import People
from django.contrib.auth.models import User
from .models import Profile #import Profile from models.py
from .models import PeopleProfile #import Profile from models.py
# class PeopleForm(forms.ModelForm):
#     email = forms.EmailField()
#     class Meta:
#         model = People
#         fields = ['username', 'surname', 'email', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'last_name', 'password')

class ProfileForm(forms.ModelForm):
	class Meta: 
		model = Profile
		fields = ('peopleform',)        

class PersonForm(forms.ModelForm):
    # butt = forms.ChoiceField(choices=PeopleProfile.YES_NO_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = PeopleProfile   
        fields = "__all__"      
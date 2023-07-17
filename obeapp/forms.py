from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Userform
from django.forms import DateInput


# Create your forms here.


class NewUserForm(UserCreationForm):

	class Meta:
		model = Userform
		fields = ("username", "email","Designation","DateofJoinning","Biometricid","password")
		widgets = {
			 'DateofJoinning':DateInput(attrs={'type':'date'}),
			 
		}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()

from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'email']

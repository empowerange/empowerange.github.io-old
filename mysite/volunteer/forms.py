from django import forms
from django.contrib.auth.models import User
from volunteer.models import UserProfileInfo

NGO_CHOICES = (
	('one', 'ONE'),
	('two', 'TWO'),
	('three', 'THREE'),)

class UserForm(forms.ModelForm):
	ngo = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=NGO_CHOICES)

	class Meta():
		model = User
		fields = ('ngo','email','first_name','last_name','username')





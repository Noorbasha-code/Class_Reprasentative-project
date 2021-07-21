from django import forms
from .models import Student1



class Studentform(forms.ModelForm):

	class Meta:
		
		model=Student1
		fields='__all__'
		# fields=['name','rollno','subjects']




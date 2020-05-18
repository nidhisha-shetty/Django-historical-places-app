from django import forms
from .models import Places

class Form(forms.ModelForm):
	place_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Add name of the place"}))
	place_ratings = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Add ratings to the place"}))
	place_description = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Add description of the place"}))

	class Meta:
		model = Places
		fields = [

			'place_name',
			'place_ratings',
			'place_image',
			'place_description'

		] 
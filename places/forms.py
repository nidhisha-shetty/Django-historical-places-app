from django import forms
from .models import Places

class Form(forms.ModelForm):
	class Meta:
		model = Places
		fields = [

			'place_name',
			'place_ratings',
			'place_image',
			'place_description'

		] 
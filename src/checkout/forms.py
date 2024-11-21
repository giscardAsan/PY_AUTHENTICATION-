from django import forms
from .models import Checkout


# creating a form
class CheckoutForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Checkout

		# specify fields to be used
		fields = [
            "email",
			"first_name",
            "surname",
			"last_name",
            "address",
            ]

		
		
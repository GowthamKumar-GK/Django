from django import forms

class IngredientForm(forms.Form):
    ingredients = forms.CharField(label='Enter ingredients you have (comma separated)', max_length=255)

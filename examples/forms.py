from django import forms
import autocomplete_light
from models import Drink

class AutocompleteForm(forms.Form):
    drink = forms.CharField(
        widget=autocomplete_light.ChoiceWidget('DrinkAutocomplete'))



from django import forms
import autocomplete_light
from models import Drink

class AutocompleteForm(forms.Form):
    drink = forms.CharField(
        widget=autocomplete_light.ChoiceWidget('drinks_autocomplete'))

    ingredients = forms.CharField(
        widget=autocomplete_light.MultipleChoiceWidget('ingredients_autocomplete')
    )

class DrinkCreateForm(forms.ModelForm):
    """ ModelForm to demonstrate how to change widget
    """
    class Meta:
        model = Drink
        widgets = {
           'ingredients': autocomplete_light.MultipleChoiceWidget('ingredients_autocomplete'),
        }



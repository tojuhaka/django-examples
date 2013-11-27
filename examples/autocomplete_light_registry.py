from models import Drink, DrinkIngredient
import autocomplete_light


class DrinkAutocomplete(autocomplete_light.AutocompleteListBase):
    choices = Drink.objects.all()

    search_fields = ['name']

# AutocompleteModelBase seems to be the right one when choices are mode objects
class IngredientAutocomplete(autocomplete_light.AutocompleteModelBase):
    choices = DrinkIngredient.objects.all()
    search_fields = ['name']


autocomplete_light.register(DrinkAutocomplete, name="drinks_autocomplete")
autocomplete_light.register(IngredientAutocomplete, name="ingredients_autocomplete")


from models import Drink
import autocomplete_light


class DrinkAutocomplete(autocomplete_light.AutocompleteListBase):
    choices = Drink.objects.all()

    search_fields = ['name']

autocomplete_light.register(DrinkAutocomplete)


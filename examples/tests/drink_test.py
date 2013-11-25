"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, RequestFactory

from examples.models import Drink
from django.test import Client
import examples.autocomplete_light_registry
from examples.views import DrinksView
from django.core.urlresolvers import resolve


def setup_view(view, request, *args, **kwargs):
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view

class DrinkTestCase(TestCase):

    def setUp(self):
        drink = Drink.objects.create(name="Margarita")
        Drink.objects.create(name="Rumcola").save()
        self.test_id = drink.id

    def test_drink(self):
        drink = Drink.objects.get(name="Margarita")
        self.assertEqual(drink.name, "Margarita")

    def test_drink_ingredients(self):
        drink = Drink.objects.get(name="Margarita")
        drink.drinkingredient_set.create(name="Tequila", amount=2)
        drink.drinkingredient_set.create(name="Cointreau", amount=2)

        ingredients = drink.drinkingredient_set.all()

        self.assertTrue("Tequila" in [i.name for i in ingredients])
        self.assertTrue("Cointreau" in [i.name for i in ingredients])

    def test_drink_list(self):
        c = Client()
        response = c.get('/examples/drinks/')
        self.assertEquals(response.status_code, 200)

    def test_drink_detail_status(self):
        response = self.client.get('/examples/drinks/'+str(self.test_id)+'/')
        self.assertEqual(response.status_code, 200)

    def test_drink_detail_status_404(self):
        response = self.client.get('/examples/drinks/15/')
        self.assertEqual(response.status_code, 404)

    def test_unit_drinks_view(self):
        request = RequestFactory().post('/fake-path', data={'drink_name': 'changed'})

        view = setup_view(DrinksView(), request)
        context = view.get_context_data(object_list=[1,2,3])
        self.assertTrue('search_form' in context)


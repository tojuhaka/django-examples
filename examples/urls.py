from django.conf.urls import patterns, url
from examples.models import Drink
from examples.views import DrinkDetailView, DrinkView,DrinkUpdateView,DrinkCreateView, RandomDrinkJsonView, DrinksView
from django.views.generic import ListView


urlpatterns = patterns('',
    url(r'^drinks.json', RandomDrinkJsonView.as_view()),
    url(r'^drinks/$', DrinksView.as_view()),
    url(r'^drinks/(?P<pk>\d+)/$', DrinkDetailView.as_view(), name="examples.views.drink.detail"),
    url(r'^drinks/(?P<pk>\d+)/edit/$', DrinkUpdateView.as_view(), name="examples.views.drink.update"),
    url(r'^drinks/add/$', DrinkCreateView.as_view(), name="examples.views.drink.create"),

)

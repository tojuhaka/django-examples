from django.core.urlresolvers import reverse
from django.db import models


class DrinkIngredient(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Drink(models.Model):
    ingredients = models.ManyToManyField(DrinkIngredient)

    name = models.CharField(max_length=200)
    test = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('examples.views.drink.detail', kwargs={'pk': self.pk})




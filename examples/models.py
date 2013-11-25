from django.core.urlresolvers import reverse
from django.db import models


class Drink(models.Model):

    name = models.CharField(max_length=200)
    test = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('examples.views.drink.detail', kwargs={'pk': self.pk})


class DrinkIngredient(models.Model):

    drink = models.ForeignKey(Drink)

    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)

    def __unicode__(self):
        return self.amount + "cl " + self.name


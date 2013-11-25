# some_app/views.py
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.detail import BaseDetailView
from examples.forms import AutocompleteForm
from examples.models import Drink
from django.utils import simplejson as json
from django import http
from django.shortcuts import get_object_or_404, render_to_response, render
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView, CreateView


class JSONResponseMixin(object):
    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        names = map(lambda x: x.name, context)
        return json.dumps(names)


class DrinkDetailView(DetailView):
    template_name = "examples/drink_detail.html"
    model = Drink



class DrinkCreateView(CreateView):
    template_name = "examples/drink_create.html"
    model = Drink


class DrinkUpdateView(UpdateView):
    template_name = "examples/drink_update.html"
    model = Drink

class DrinksView(ListView):
    queryset=Drink.objects.all()
    context_object_name="drinks"
    template_name="/examples/drink_list.html"

    def get_context_data(self, **kwargs):
        context = super(DrinksView, self).get_context_data(**kwargs)
        context['search_form'] = AutocompleteForm()
        return context





class RandomDrinkJsonView(JSONResponseMixin, TemplateView):

    def get_context_data(self, **kwargs):
        return Drink.objects.all()


class DrinkView(DetailView):
    queryset = Drink.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(DrinkView, self).get_object()
        # Record the last accessed date
        object.last_accessed = "asdf!"
        object.save()
        # Return the object
        return object

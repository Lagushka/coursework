from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from forms.models import Category, Form

class IndexView(generic.ListView):
    template_name = 'forms/index.html'
    model = Category
    context_object_name = 'category_list'

class CategoryView(generic.DetailView):
    template_name = 'forms/category.html'
    model = Category

class FormView(generic.DetailView):
    template_name = 'forms/form.html'
    model = Form



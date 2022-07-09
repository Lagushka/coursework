from unicodedata import name
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from forms.models import Category, Form, Answer, Passed_Form, User

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

class PassedView(generic.ListView):
    template_name = 'forms/passed.html'
    model = User
    context_object_name = 'user_list'

class PassedFormView(generic.DetailView):
    template_name = 'forms/passed_form.html'
    model = Passed_Form

class UserView(generic.DetailView):
    template_name = 'forms/user.html'
    model = User

def submit(request, form_id):
    new_form = get_object_or_404(Form, pk=form_id)
    try:
        username = User.objects.get(name=request.POST.get("name", "noname"))
    except:
        username = User(name=request.POST.get("name", "noname"))
    username.save()
    new_passed_form = Passed_Form(form=new_form, user=username)
    new_passed_form.save()
    for new_question in new_form.questions.all():
        print(request.POST.get(str(new_question.id), new_question.id))
        answer = Answer(passed_form=new_passed_form, question=new_question, text=request.POST.get(str(new_question.id), "has not been got"))
        answer.save()
    return HttpResponseRedirect(reverse('forms:index', args=()))





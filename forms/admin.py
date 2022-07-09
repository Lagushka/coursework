import site
from django.contrib import admin

from .models import Category, Form, Question, Passed_Form, Answer, User

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Passed_Form)
admin.site.register(Answer)
admin.site.register(Form)
admin.site.register(User)
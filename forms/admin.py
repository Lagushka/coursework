import site
from django.contrib import admin

from .models import Category, Form, Question, Passed_Form, Answer, User

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_forms')

    def get_forms(self, obj):
        return [f.name for f in obj.forms.all()]

    get_forms.short_description = 'Формы'

class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_questions')

    def get_questions(self, obj):
        return [q.text for q in obj.questions.all()]
    
    get_questions.short_description = 'Вопросы'

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Passed_FormAdmin(admin.ModelAdmin):
    list_display = ('get_name',)

    def get_name(self, obj):
        return obj.form.name

    get_name.short_description = 'Вопросы'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Passed_Form, Passed_FormAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(User, UserAdmin)
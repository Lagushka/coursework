from tabnanny import verbose
from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=1024, verbose_name="Текст")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Вопросы"

class Form(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    pub_date = models.DateTimeField('date published')
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Анкеты"
        
class User(models.Model):
    name = models.CharField(max_length=100, default="noname", verbose_name="Имя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Пользователи"

class Passed_Form(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.form.name

    class Meta:
        verbose_name_plural = "Пройденные формы"

class Answer(models.Model):
    passed_form = models.ForeignKey(Passed_Form, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name="Текст")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Ответы"

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    forms = models.ManyToManyField(Form)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
    

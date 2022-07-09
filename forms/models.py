from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=1024)

    def __str__(self):
        return self.text

class Form(models.Model):
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name
        
class User(models.Model):
    name = models.CharField(max_length=100, default="noname")

    def __str__(self):
        return self.name

class Passed_Form(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.form.name

class Answer(models.Model):
    passed_form = models.ForeignKey(Passed_Form, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length=255)
    forms = models.ManyToManyField(Form)

    def __str__(self):
        return self.name
    

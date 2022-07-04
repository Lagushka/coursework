from cgitb import text
from pyexpat import model
from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.CharField(max_length=1024)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Passed_Form(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

class Answers(models.Model):
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
    

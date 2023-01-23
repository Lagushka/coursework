from rest_framework import serializers
from forms.models import Category, Form, Passed_Form, User, Answer

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['name', 'forms']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['name']

class FormSerializer(serializers.ModelSerializer):
  class Meta:
    model = Form
    fields = ['name', 'pub_date', 'questions']

class AnswerSerializer(serializers.ModelSerializer):
  passed_form = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
  question = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

  class Meta:
    model = Answer
    fields = ['passed_form', 'question', 'text']

class PassedSerializer(serializers.ModelSerializer):
  form = FormSerializer(many=False, read_only=True)
  user = UserSerializer(many=False, read_only=True)
  answer = AnswerSerializer(many=True, read_only=True)

  class Meta:
    model = Passed_Form
    fields = ['form', 'user', 'answer']
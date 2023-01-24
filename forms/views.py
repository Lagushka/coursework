from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.filters import SearchFilter
from forms.serializers import CategorySerializer, FormSerializer, PassedSerializer, UserSerializer, AnswerSerializer
from django.db.models import Q
from django.views import generic
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from forms.models import Category, Form, Answer, Passed_Form, User, Question

class IndexView(generic.ListView):
    template_name = 'forms/index.html'
    model = Category
    context_object_name = 'category_list'

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FormsViewPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10
class FormView(ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    pagination_class = FormsViewPagination

    @action(methods=['GET'], detail=True)
    def form_search(self, _, **kwargs):
        value = kwargs.get('pk')
        
        if not value:
            raise NotFound({'error': 'no value no gain'})

        got_forms = Passed_Form.objects.filter(Q(form=value))

        serializer = PassedSerializer(data=got_forms, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def last_forms(self, _):
        last_forms = Form.objects.all().order_by('-pub_date')
        page = self.paginate_queryset(last_forms)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = FormSerializer(data=last_forms, many=True)
        serializer.is_valid()
        return Response(serializer.data)
class PassedView(ModelViewSet):
    queryset = Passed_Form.objects.all()
    serializer_class = PassedSerializer

    @action(methods=['POST'], detail=False)
    def add_passed_form(self, request):
        try:
            curForm = get_object_or_404(Form, pk=request.data.get('id'))
        except:
            raise NotFound({'error': 'form not found' + str(request.data.get('id'))})

        if request.data.get('user') and request.data.get('user') != '':
            try:
                username = User.objects.get(name=request.data.get('user'))
            except:
                username = User(name=request.data.get('user'))
                username.save()
        else: 
            raise ValidationError({'error': 'username must not be empty'})

        new_passed_form = Passed_Form(form = curForm, user = username)
        new_passed_form.save()
        for answer in request.data.get('answers'):
            if answer.get('text') and answer.get('text') != '':
                new_answer = Answer(passed_form = new_passed_form, question = get_object_or_404(Question, pk=answer.get('question_id')), text = answer.get('text'))
                new_answer.save()
            else:
                raise ValidationError({'error': 'all questions should be answered'})
        
        return Response({"message": "form successfully added"})
class AnswerView(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['text']
class UserView(ModelViewSet):
    queryset = User.objects.all().order_by('-name')
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ['id']
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from forms.serializers import CategorySerializer, FormSerializer, PassedSerializer, UserSerializer, AnswerSerializer
from django.urls import reverse
from django.views import generic

from forms.models import Category, Form, Answer, Passed_Form, User

class IndexView(generic.ListView):
    template_name = 'forms/index.html'
    model = Category
    context_object_name = 'category_list'

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FormsViewPagination(PageNumberPagination):
    page_size = 15
    page_query_param = 'page_size'
    max_page_size = 15
class FormView(ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    pagination_class = FormsViewPagination

    @action(methods=['GET'], detail=False)
    def last_forms(self, _):
        last_forms = Form.objects.all().order_by('-pub_date')
        page = self.paginate_queryset(last_forms)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(last_forms, many=True)
        return Response(serializer.data)

class PassedView(ModelViewSet):
    queryset = Passed_Form.objects.all()
    serializer_class = PassedSerializer

    # @action(methods=['POST'], detail=True)
    # def addPassedForm(self, request, pk=None):
    #     data = request.data
        

class AnswerView(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
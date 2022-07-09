from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('form/<int:pk>/', views.FormView.as_view(), name='form'),
    path('form/<int:form_id>/submit/', views.submit, name='submit'),
    path('passed/', views.PassedView.as_view(), name='passed'),
    path('passed_form/<int:pk>/', views.PassedFormView.as_view(), name='passed_form'),
    path('user/<int:pk>', views.UserView.as_view(), name='user'),
]
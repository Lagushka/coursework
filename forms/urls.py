from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('form/<int:pk>/', views.FormView.as_view(), name='form')
]
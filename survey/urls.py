from django.urls import path
from . import views

app_name = 'survey'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:question_sort>/', views.main, name='main'),
    path('<str:question_sort>/answer/', views.answer, name='answer'),
    path('<str:question_sort>/Detail/', views.Detail, name='Detail'),
    path('<str:question_sort>/Next/', views.Next, name='Next'),
    path('<str:question_sort>/save_survey/', views.save_survey, name='save_survey'),
]
from django.urls import path

from . import views

app_name = 'foodAllergy'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:allergy_id>/', views.detail, name='detail'),
    path('register/', views.allergy_register, name='register'),

    #allergy에 db저장하기
    path('regist/', views.regist, name='regist'),
]

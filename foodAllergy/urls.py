from django.urls import path

from . import views

app_name = 'foodAllergy'

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:allergy_id>/', views.detail, name='detail'),

    path('register/', views.allergy_register, name='register'),

    # allergy에 db저장하기
    path('regist/', views.regist, name='regist'),

    path('register/<str:allergy_name>/', views.showLv2, name='showLv2'),

    path('register/myAllergy/<str:allergy_name>/', views.myshowLv2, name='myshowLv2'),

    path('register/addMyAllergy', views.addMyAllergy, name='addMyAllergy'),

    path('register/deleteMyAllergy', views.deleteMyAllergy, name='deleteMyAllergy'),
    # -------------------------------------------------------------------------------------

    # 불러오기 창이동
    path('resultLoad/',views.resultLoad, name='resultLoad'),

    path('resultLoad/<str:result_name>/', views.detailResult, name='detailResult'),

    path('saveResult',views.resultSave, name='resultSave'),

    path('chImage', views.chImage, name='chImage'),

]

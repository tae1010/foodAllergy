from django.urls import path
from .import views
urlpatterns=[
    path('',views.index),
    path('<int:Result_id>/',views.detail),
]
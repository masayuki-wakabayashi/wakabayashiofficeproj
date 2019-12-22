from django.urls import path
from . import views

urlpatterns = [
    path('send/<int:office_id>/', views.send, name='send'),
    path('form', views.form, name='form'),
]
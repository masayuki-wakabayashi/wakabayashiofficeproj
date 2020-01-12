from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:office_id>/', views.post, name='post'),
    path('form', views.form, name='form'),
    path('list/', views.list, name='list'),
]
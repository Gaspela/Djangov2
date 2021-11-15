from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_Form),
    path('list/', views.employee_List),
    path('delete/', views.employee_Delete)

]

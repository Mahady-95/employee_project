from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.employee_form,name='employee_insert'),
    path('<int:id>/',views.employee_form,name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list,name='employee_list'),

    path('pdf/', views.employee_pdf, name='employee_pdf'),
    path('excel/', views.employee_excel, name='employee_excel'),
    path('chart/', views.employee_chart, name='employee_chart'),


   

]
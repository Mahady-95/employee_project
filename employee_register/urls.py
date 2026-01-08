from django.urls import path, include
from . import views

urlpatterns = [
    # path('',views.employee_form,name='employee_insert'),
    # path('<int:id>/',views.employee_form,name='employee_update'),
    # path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    # path('list/', views.employee_list,name='employee_list'),

    # path('pdf/', views.employee_pdf, name='employee_pdf'),
    # path('excel/', views.employee_excel, name='employee_excel'),
    # path('chart/', views.employee_chart, name='employee_chart'),
    # # path('login/'views.)

    # path('', views.employee_form, name='employee_list'),            # /employee/
    # path('add/', views.employee_form, name='employee_insert'),      # /employee/add/
    # path('<int:id>/', views.employee_form, name='employee_update'), # /employee/update/1
    # path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    # path('pdf/', views.employee_pdf, name='employee_pdf'),
    # path('excel/', views.employee_excel, name='employee_excel'),
    # path('chart/', views.employee_chart, name='employee_chart'),

    path('', views.employee_form, name='employee_insert'),                  # add new employee
    path('<int:id>/', views.employee_form, name='employee_update'),         # update employee
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),# delete employee
    path('list/', views.employee_list, name='employee_list'),               # employee list

    path('pdf/', views.employee_pdf, name='employee_pdf'),                  # download pdf
    path('excel/', views.employee_excel, name='employee_excel'),            # download excel
    path('chart/', views.employee_chart, name='employee_chart'),            # chart
    path('dashboard/', views.dashboard, name='dashboard'),


   

]
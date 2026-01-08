from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee, Position
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from openpyxl import Workbook

import matplotlib.pyplot as plt
import io
import base64
from django.db.models import Count

from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required





# Create your views here.
# Search + Pagination
@login_required
def employee_list(request):
    print("EMPLOYEE LIST VIEW HIT")
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', 'name')

    employees = Employee.objects.all()

    if q:
        employees = employees.filter(
            Q(fullname__icontains=q) |
            Q(mobile__icontains=q) |
            Q(position__title__icontains=q)
        )

    if sort == 'position':
        employees = employees.order_by('position__title')
    else:
        employees = employees.order_by('fullname')

    paginator = Paginator(employees, 5)
    page = request.GET.get('page')
    employee_list = paginator.get_page(page)

    return render(request, 'employee_register/employee_list.html', {
        'employee_list': employee_list,
        'search_query': q,
        'sort': sort,
    })

@login_required
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list') 
    
@login_required
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list') 


@login_required
def employee_pdf(request):
    employees = Employee.objects.all()

    template = get_template('employee_register/employee_pdf.html')
    html = template.render(
        {'employee_list': employees},   # ✅ SAME NAME
        request=request
    )

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="employee_report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF Error')

    return response



@login_required
def employee_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Employee Report"

    # 🔹 Header row
    ws.append(["Full Name", "Mobile", "Position"])

    # 🔹 Data rows
    employees = Employee.objects.all()
    for emp in employees:
        ws.append([
            emp.fullname,
            emp.mobile,
            str(emp.position)   # ForeignKey safe
        ])

    # 🔹 Response
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=employee_report.xlsx'

    wb.save(response)
    return response






@login_required
def employee_chart(request):
    # Group data
    data = (
        Employee.objects
        .values('position__title')
        .annotate(total=Count('id'))
    )

    positions = [item['position__title'] for item in data]
    totals = [item['total'] for item in data]

    # Create chart
    plt.figure(figsize=(6,4))
    plt.bar(positions, totals)
    plt.xlabel('Position')
    plt.ylabel('Number of Employees')
    plt.title('Employees by Position')

    # Save chart to memory
    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close()

    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'employee_register/employee_chart.html', {
        'chart': graphic
    })

#Dashboard

def dashboard(request):
    total_employees = Employee.objects.count()
    total_positions = Position.objects.count()

    recent_employees = Employee.objects.select_related(
        'position'
    ).order_by('-id')[:5]

    chart_data = (
        Employee.objects
        .values('position__title')
        .annotate(total=Count('id'))
    )

    return render(request, 'employee_register/dashboard.html', {
        'total_employees': total_employees,
        'total_positions': total_positions,
        'recent_employees': recent_employees,
        'chart_data': chart_data
    })
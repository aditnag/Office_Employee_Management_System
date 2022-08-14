from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'emp_app/index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    print(context)
    return render(request, 'emp_app/view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        dept = request.POST['dept']
        bonus = request.POST['bonus']
        role = request.POST['role']
        phno = request.POST['phone']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, dept_id=dept, role_id=role, phno=phno, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully!")
    else:
        return render(request, 'add_emp.html')


def remove_emp(request):
    return render(request, 'emp_app/remove_emp.html')


def filter_emp(request):
    return render(request, 'emp_app/filter_emp.html')

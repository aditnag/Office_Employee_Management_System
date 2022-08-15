from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Employee, Role, Department
from datetime import datetime
from django.urls import reverse


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
        salary = int(request.POST['salary'])
        dept = int(request.POST['dept'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, dept_id=dept,
                           role_id=role, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully!")
        # return HttpResponseRedirect(reverse('emp_app:index', args=(new_emp.id,)))
    elif request.method == 'GET':
        return render(request, 'emp_app/add_emp.html')
    else:
        return HttpResponse("An Exception Occurred! Employee has not been added")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully!")
        except:
            return HttpResponse("Please enter a valid Employee id")
    emps = Employee.objects.all()
    contex = {
        'emps': emps
    }
    return render(request, 'emp_app/remove_emp.html', contex)


def filter_emp(request):
    return render(request, 'emp_app/filter_emp.html')

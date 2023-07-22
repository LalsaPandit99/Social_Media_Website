from django.shortcuts import render
from django.views.generic.list import ListView
from .models import EmployeeData


class EmployeeRetrieve(ListView):
    model = EmployeeData


def employee_list(request):
    emp_list = EmployeeData.object.all()
    return render(request, 'employeelist.html', {'emp_list': emp_list})
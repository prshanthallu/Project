from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


def f(request):
    emp_list = Employee.objects.all()

    return render(request, "home.html", context={'emp_list': emp_list})

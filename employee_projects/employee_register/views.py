from django.shortcuts import render

# Create your views here.

def employee_List(request):
    return render(request,"employee_register/employee_list.html")

def employee_Form(request):
    return render(request,"employee_register/employee_form.html")

def employee_Delete(request):
    return

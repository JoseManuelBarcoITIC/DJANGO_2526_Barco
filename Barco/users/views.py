from django.shortcuts import render,redirect

from .models import User
from .forms import UserForm


def getAllStudents(request):
    allStudents = User.objects.filter(type=1)
    response = {"persons":allStudents}
    return render(request, 'main_page.html',response)

def getAllTeachers(request):
    allTeachers= User.objects.filter(type=2)
    response = {"persons":allTeachers}
    return render(request, 'main_page.html',response)

def user_form(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('select_students')

    context = {"form": form}
    return render(request,'form.html',context)

def update_user (request,pk):
    user_id = User.objects.get(id=pk)
    form = UserForm(instance=user_id)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('select_students')

    context = {"form":form}
    return render(request, 'form.html',context)
def delete_user (request,pk):
    user_id = User.objects.get(id=pk)

    if request.method == "POST":
        user_id.delete()
        return redirect ('select_students')
    context = {"form":user_id}
    return render(request, 'delete_user.html',context)

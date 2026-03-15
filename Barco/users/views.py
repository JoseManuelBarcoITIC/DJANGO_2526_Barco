from django.shortcuts import render

from .models import User


def getAllStudents(request):
    allStudents = User.objects.filter(type=1)
    response = {"persons":allStudents}
    return render(request, 'main_page.html',response)

def getAllTeachers(request):
    allTeachers= User.objects.filter(type=2)
    response = {"persons":allTeachers}
    return render(request, 'main_page.html',response)



from django.shortcuts import render

def getAllStudents(request,role):
    allUsers = Person.objects.all()
    response = {"persons":allUsers}
    return render(request, 'main_page.html',response)



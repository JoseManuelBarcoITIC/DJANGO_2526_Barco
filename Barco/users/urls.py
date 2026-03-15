
from django.urls import path
from . import views
urlpatterns = [
    path('students/',views.getAllStudents ,name='select_students'),
    path('teachers/', views.getAllTeachers, name='select_teachers'),

]

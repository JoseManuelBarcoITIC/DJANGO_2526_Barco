
from django.urls import path
from . import views
urlpatterns = [
    path('students/',views.getAllStudents ,name='students'),
    path('teachers/', views.getAllStudents, name='teachers'),

]

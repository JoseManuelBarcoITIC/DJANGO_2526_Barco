
from django.urls import path
from . import views
urlpatterns = [
    path('students/',views.getAllStudents ,name='select_students'),
    path('teachers/', views.getAllTeachers, name='select_teachers'),
    path('create_user/', views.user_form, name='user_form'),
    path('update_users/<int:pk>',views.update_user, name="update_u"),
    path('delete_user/<int:pk>', views.delete_user, name="delete_u")

]


from django.shortcuts import render

def students(request):
    students_list = {
        'student1':{
            'id':1,
            'name':'Jose',
            'surname': 'Barco',
            'email': 'jose.barco@iticbcn.cat',
            'rol': 'student'
    },
        'student2': {
            'id': 2,
            'name': 'Josep',
            'surname': 'Bona',
            'email': 'josep.bona@iticbcn.cat',
            'rol': 'student'
    },
        'student3': {
            'id': 3,
            'name': 'Pepe',
            'surname': 'Bona',
            'email': 'pepe.bona@iticbcn.cat',
            'rol': 'student'
    },
        'student4': {
            'id': 3,
            'name': 'Erik',
            'surname': 'Llorens',
            'email': 'erik.llorens@iticbcn.cat',
            'rol': 'student'
    }
    }
    info = {'msg':students_list}
    return render(request,'main_page.html',info)
from django.shortcuts import render

def teachers(request):
    teacher_list = {
        'teacher1':{
            'id':1,
            'name':'Roger',
            'surname': 'Sobrino',
            'email': 'roger.sobrino@iticbcn.cat',
            'rol': 'teacher'
    },
        'teacher2': {
            'id': 2,
            'name': 'Oriol',
            'surname': 'Roca',
            'email': 'joriol.roca@iticbcn.cat',
            'rol': 'teacher'
    },
        'teacher3': {
            'id': 3,
            'name': 'Pepe',
            'surname': 'Pepazo',
            'email': 'pepe.pepazo@iticbcn.cat',
            'rol': 'teacher'
    },
        'teacher4': {
            'id': 4,
            'name': 'Antonio',
            'surname': 'Jurado',
            'email': 'antonio.jurado@iticbcn.cat',
            'rol': 'teacher'
    },
    }
    info = {'msg':teacher_list}
    return render(request,'main_page.html',info)
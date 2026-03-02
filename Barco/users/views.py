from django.shortcuts import render

# Create your views here.
def users(request):
    user_list = {
        'user1':{
            'id':1,
            'name':'Jose',
            'email': 'jose.barco@iticbcn.cat',
            'rol': 'student'
    },
        'user2': {
            'id': 1,
            'name': 'Josep',
            'email': 'josep.bona@iticbcn.cat',
            'rol': 'student'
    },
      'user2': {
            'id': 1,
            'name': 'Josep',
            'email': 'josep.bona@iticbcn.cat',
            'rol': 'student'
    },
    }
    info = {'msg':user_list}
    return render(request,'main_page.htlm',info)
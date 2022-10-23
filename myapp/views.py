from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

# Create your views here.
def index(request):
    user = User.objects.all()
    context = {'users':user}
    print(context)

    return render(request,"index.html", context)

## 新規登録
def login(request):
    return render(request, "login.html")

def save(request):
    template = loader.get_template('save.html')
    try :
        user = User.objects.Create(
            id = request.POST['userid'],
            password = request.POST['userpasswrod'],
            username = request.POST['username'],
            age = request.POST['age'],
            sex = request.POST['sex'],
            email = request.POST['email']
        )
    except IntegrityError as e :
        context = {
            'user': request.POST,
            'error_message': "存在しているユーザーです。",
        }
    return HttpResponse(template.render(context,request))
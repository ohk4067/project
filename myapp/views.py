from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
from datetime import datetime


# Create your views here.
def index(request):
        # post = Post.objects.all()
        post = Post.objects.order_by('-no')
        context = {'posts':post}
        return render(request,"index.html", context)

## Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Login error"
            return render(request, 'login.html',{'error_message': error_message})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

## Signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

## Write
def write(request):
    if request.method == 'POST': 
        todays = datetime.now()
        title = request.POST.get('title')
        message = request.POST.get('message')
        image = request.POST.get('image')
        writer = request.POST.get('writer')
        my_data = Post(title=title, message=message, image=image, writer=writer,date=todays)
        my_data.save()
        return redirect("index")
    return render(request, 'write.html')

def posting(request, no):
    post = Post.objects.get(no=no)
    return render(request, 'posting.html', {'post':post})

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴 
    return render(request, 'blog.html', {'postlist':postlist})

def save(request):
    # template = loader.get_template('save.html')
    # try :
    #     user = User.objects.Create(
    #         id = request.POST['userid'],
    #         password = request.POST['userpasswrod'],
    #         username = request.POST['username'],
    #         age = request.POST['age'],
    #         sex = request.POST['sex'],
    #         email = request.POST['email']
    #     )
    # except IntegrityError as e :
    #     context = {
    #         'user': request.POST,
    #         'error_message': "存在しているユーザーです。",
    #     }
    return render(request, "save.html")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
from datetime import datetime

# Create your views here.
def index(request):
        user = User.objects.all()
        context = {'users':user}
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
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "index.html")
    else:
        form = PostForm()
    return render(request, 'write.html', {'form': form})

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴 
    return render(request, 'blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})

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
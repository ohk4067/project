from django.shortcuts import render
from django.http import HttpResponse

from .models import User

# Create your views here.
def test(request):
    user = User.objects.all()
    context = {'users':user}
    print(context)

    return render(request, "test.html", context)

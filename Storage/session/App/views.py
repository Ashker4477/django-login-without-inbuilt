from django.shortcuts import render
from .models import User
from django.http import HttpResponse


def home (request):
    return render(request, 'Login.html')


def login (request):
    m = User.objects.get(Name=request.POST['user'])
    if m.password == request.POST['psw']:
        request.session['member_id'] = m.id
        return render(request, 'User.html')
    else:
        return HttpResponse("Your username and password didn't match.")


def logout (request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return render(request, 'Login.html')


def signup (request):
    return render(request, 'Signup.html')


def Success (request):
    a = request.FILES['profile']
    b = request.POST['name']
    c = request.POST['Dob']
    d = request.POST['em']
    e = request.POST['psw']
    data = User(Profile=a, Name=b, DateOfBirth=c, Email=d, password=e)
    data.save()
    return render(request, 'Success.html')

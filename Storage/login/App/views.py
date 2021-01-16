from django.shortcuts import render
from .models import reg


# Create your views here.
def home (request):
    return render(request, 'login.html')


def register (request):
    return render(request, 'register.html')


def book (request):
    data = reg.objects.all()
    return render(request, 'Book.html', {'name':data})


def succ (request):
    a = request.POST['fn']
    b = request.POST['ln']
    c = request.POST['em']
    d = request.POST['Dob']
    e = request.FILES['img']
    data = reg(fn=a, ln=b, em=c, Dob=d, img=e)
    data.save()
    return render(request, 'Success.html')




def Search (request):
    return render(request, 'Search.html')


def result (request):
    l = request.POST['q']
    data = reg.objects.filter(fn=l)
    return render(request, "Result.html", {'name': data})

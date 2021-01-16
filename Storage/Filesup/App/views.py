from django.shortcuts import render
from .models import Register


# Create your views here.

def home (request):
    return render(request, 'Fileup.html')


def success (request):
    a = request.POST['name']
    b = request.FILES['file']
    data = Register(Fullname=a, Profile=b)
    data.save()
    return render(request, 'Success.html')


def view(request):
    data = Register.objects.all()
    return render(request, 'view.html', {'name': data})
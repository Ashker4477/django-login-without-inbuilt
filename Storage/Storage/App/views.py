from django.shortcuts import render
from .models import regist


# Create your views here.
def home (request):
    return render(request, "register.html")


def reg (request):
    a = request.POST['fname']
    b = request.POST['lname']
    c = request.POST['Age']
    d = request.POST['sex']
    e = request.POST['DOB']
    f = request.POST['em']
    g = request.POST['address']
    h = request.POST['Country']
    i = request.POST['State']
    j = request.POST['District']
    k = request.POST['Pincode']
    l = request.POST['city']
    data = regist(fname=a, lname=b, Age=c, sex=d, DOB=e, em=f, address=g, Country=h, State=i, District=j, Pincode=k,
                  city=l)
    data.save()
    data=regist.objects.all()
    return render(request, "reg.html", {'name':data})

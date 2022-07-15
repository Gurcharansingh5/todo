from django.shortcuts import render,HttpResponse,redirect
from ecommerceadmin.models import *
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    allproducts = product.objects.all()
    print(allproducts)
    return render(request,'index.html',{'allproducts':allproducts})
def register(request):
    if request.method == 'POST':
        usernames = request.POST['usernames']
        email = request.POST['email']
        passwords = request.POST['passwords']
        print(usernames,passwords)
        User.objects.create_user(username=usernames,password=passwords,email=email)

        return redirect('index')
    else:
        return render(request,'register.html')

def authlogin(request):
    if request.method == 'POST':
        usernames = request.POST['usernames']
        passwords = request.POST['passwords']
        print(usernames,passwords)
        user = authenticate(request, username=usernames, password=passwords)
        login(request,user)
        return redirect('index')
            # return redirect('authenticate')
    else:
        return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return  redirect('index')

def purchase(request,id):
    productid = product.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        purchasesave = buy(
            name = name,
            phone = phone,
            address = address,
            productid = productid,
            userid = request.user,
        )
        purchasesave.save()
        return HttpResponse('booked successfull')
    else:
        return render(request,'buy.html',{'id':id,'productid':productid})

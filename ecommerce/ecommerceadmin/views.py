from django.shortcuts import render,HttpResponse
from . models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/authlogin')
def adminindex(request):
    if request.method == 'POST':
        product_images = request.FILES['image']
        name = request.POST['name']
        price = request.POST['price']
        datasave = product(
            productname = name,
            productimage = product_images,
            productprice = price
        )
        datasave.save()

        return HttpResponse(' data uploaded succesfly')
    else:
        return render(request,'adminindex.html')

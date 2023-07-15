from django.shortcuts import render,redirect
import uuid
from .models import Url
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def index(request):

    if request.method == 'POST':
        link = request.POST.get('link')
        if link == "":
            messages.success(request,"The url is empty")
            return redirect('home')


            
        else:
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=link,uuid=uid)
            new_url.save()
            messages.success(request,f"127.0.0.1:8000/{uid}/")

            return redirect('home')
            # return redirect('home')
    return render(request,'index.html')


def go(request, pk):
    url_details = Url.objects.filter(uuid=pk).first()
    print(url_details.link)
    return redirect('https://'+url_details.link)




    

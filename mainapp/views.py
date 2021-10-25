from django.shortcuts import redirect, render
from mainapp.models import ImagenCarrusel
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
# Create your views here.


def index(request):
    imagenes=ImagenCarrusel.objects.all()
    
    return render(request, 'index.html',{'imagenes':imagenes})

def aboutUs(request):

    return render(request, 'about-us.html')

def questionContact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        array=[]
        array.append(settings.EMAIL_HOST_USER)
        send_mail(
            'Hello, my name is: '+name+" Phone: "+phone+ " Email: "+email,
            message,
            settings.EMAIL_HOST_USER,
            array,
            fail_silently=False,
        )
        messages.success(request, 'Thanks, will be on contact to you sop soon!')
        return redirect('home')


def newAdvice(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            array=[]
            users=User.objects.all()
            for user in users:
                array.append(user.email)
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                array,
                fail_silently=False,
            )
            messages.success(request, 'New Advice sended by email!')
            return redirect('home')
        else:
            return render(request, 'new-advice.html')
    else:
        return redirect('home')
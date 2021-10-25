from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from users.forms import RegisterUserForm, ChangePass
from django.contrib.auth.models import User

# Create your views here.

def usersLogin(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "User or Password are wrong ")
                return redirect('login')

    return render(request, 'login.html')

def usersLogout(request):
    logout(request)
    return redirect('home')

def registerUser(request):

    if request.method=='POST':
        registerUserForm=RegisterUserForm(request.POST)
        if registerUserForm.is_valid():
            registerUserForm.save()
            messages.success(request, 'User registered')
            return redirect('login') 
    else:
        registerUserForm=RegisterUserForm()
    
    return render(request, 'register.html', {'form':registerUserForm})


@login_required(login_url='login')
def showUsers(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        users=User.objects.all()
        return render(request, 'list-users.html', {'users':users})

@login_required(login_url='login')
def deleteUser(request, id):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        user=User.objects.get(pk=id)
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('list-users')

@login_required(login_url='login')
def changePass(request):
    if request.method=='POST':
        cambiarForm=ChangePass(request.POST)
        if cambiarForm.is_valid():
            cambiarForm.save(commit=False)
            user = User.objects.get(username=request.user.username)
            password1=cambiarForm.cleaned_data['password1']
            password2=cambiarForm.cleaned_data['password2']
            user.set_password(password2)
            user.save()
            return redirect('home')
    else:
        cambiarForm=ChangePass()


    return render(request, 'cambiarpass.html',{'form':cambiarForm})

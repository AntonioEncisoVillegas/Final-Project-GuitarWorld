from django import forms
from django.forms import fields
#from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ChangePass(UserCreationForm):
    class Meta:
        model=User
        fields=['password1', 'password2']
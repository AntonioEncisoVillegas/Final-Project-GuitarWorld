from django.urls import path
from users import views
urlpatterns = [
    path('login/', views.usersLogin, name="login"),
    path('logout/', views.usersLogout, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('list/users/', views.showUsers, name="list-users"),
    path('user/delete/<int:id>', views.deleteUser, name="delete-user"),
    path('user/change/pass/', views.changePass, name="change-pass"),
    
]
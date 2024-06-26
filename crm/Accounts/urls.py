"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Accounts import views


urlpatterns = [
    # these are like controllers/views so we get an url (to the controller/view), method (in the
    # the controller/view) and the name of the controller/view
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home, name="home"),
    path("update_order/<str:pk>/", views.updateOrder, name="update_order"),

    path("delete_order/<str:pk>/", views.deleteOrder, name="delete_order" ),

    path("user/", views.userPage, name="user_page"),
]

from django.contrib import admin
from django.urls import path, include
from login import views
from home import urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.login, name = 'login'),
    path("signup/", views.signup, name="signup"),
    path("home/",include('home.urls')),
]
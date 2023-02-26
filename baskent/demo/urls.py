from django.urls import path
from django.contrib import admin
#now import the views.py file into this code
from . import views
urlpatterns=[
path('admin/', admin.site.urls),
path("", views.home, name="index"),
path("home/", views.home, name="home"),
path("second/", views.second, name="second"),
path("third/", views.third, name="third"),
path("form/", views.form, name="form"),
path("form/<int:id>", views.form, name="form"),
]
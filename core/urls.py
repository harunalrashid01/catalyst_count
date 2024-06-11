from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path("",views.index,name='home'),
    path("querybuilder",views.querybuilder,name='querybuilder'),
    path("user",views.user,name='user'),
    path("upload",views.upload,name='upload'),
    
]

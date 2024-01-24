from django.contrib import admin
from django.urls import path, include
from helloworldproject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("helloworld/", hello_world),
    path("helloworld2/", HelloWorld.as_view()),
    path("aaa/", include("helloworldapp.urls"))
]

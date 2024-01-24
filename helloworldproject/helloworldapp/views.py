from django.shortcuts import render
from django.http.response import HttpResponse

def hello_world_app_view(request):
    res = HttpResponse("app views")
    return res

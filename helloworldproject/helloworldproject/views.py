from django.http import HttpResponse
from django.views.generic import TemplateView



class HelloWorld(TemplateView):
    template_name = "hello_world.html"

def hello_world(request):
    res = HttpResponse("<h1>Hello world</h1>")
    return res

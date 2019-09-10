from django.shortcuts import render
from django.http import HttpResponse



# function will handle traffic from homepage of blog return what user sees when using this route


def home(request):
    return HttpResponse("<h1>Blog Home</h1>")

def about(request):
    return HttpResponse("<h1>Blog About</h1>")
# URL MAPPING PATH_--> STEP3 ... prints the response at the location



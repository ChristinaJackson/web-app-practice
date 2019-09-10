from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    #empty path, function created in the views.py file, and the name this is printed on the blog page from the views.py
    path('about/', views.about, name="blog-about")
# URL MAPPING PATH_--> STEP2 ... navs to the blogs.url (1) then the about path, this is the def about function in views.py
]


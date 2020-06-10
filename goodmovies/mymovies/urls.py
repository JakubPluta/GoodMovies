from django.urls import path
from . import views

# https://schier.co/blog/html-templating-output-a-grid-in-a-single-loop


urlpatterns = [
    path('', views.index,name='search'),
]
from django.urls import path
from . import views

# https://schier.co/blog/html-templating-output-a-grid-in-a-single-loop


urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:id>/', views.movie_details, name='movie-detail'),
    path('add_movie/', views.add_to_watchlist,name='watchlist'),
]
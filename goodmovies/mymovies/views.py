from django.shortcuts import render
import requests
import os

TMDb_KEY = os.environ.get('TMDb')



# Create your views here.

# def index(request):
#     return render(request, 'mymovies/home.html')


def fetch_movie_from_api(request=1):
    url = f'https://api.themoviedb.org/3/movie/550?api_key={TMDb_KEY}'
    r = requests.get(url).json()

    movie = {
        'id' : r['id'],
        "imdb_id": r['imdb_id'],
        'adult' : r['adult'],
        'original_language' : r['original_language'],
        "original_title": r['original_title'],
        'budget' : r['budget'],
        "overview" : r["overview"],
        'popularity' : r['popularity'],
        'img' : r['backdrop_path'],
        'genres' :  [genre.get('name') for genre in r['genres']],
        'status' : r['status'],
        'tagline' : r['tagline'],
        "title": r['title'],
        "vote_average": r['vote_average'],
        "vote_count": r["vote_count"],
    }
    context = {'movie' : movie}
    return render(request, 'mymovies/home.html',context)



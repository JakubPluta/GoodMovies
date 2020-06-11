import requests
import os
from django.shortcuts import render
from .models import MovieData

TMDb_KEY = os.environ.get('TMDb')

# https://api.themoviedb.org/3/movie/{movie_id}?api_key=TMDb_KEY


def index(request):
    movies_data = []
    MAX_RECORDS = 12

    if request.method == "POST":
        url = f'https://api.themoviedb.org/3/search/movie?'
        movie_url = f'https://api.themoviedb.org/3/movie/'

        query_params = {
            'query' : request.POST["movie_name"],
            'page' : "1",
            'language' : 'en-US',
            'api_key' : TMDb_KEY
        }
        req = requests.get(url, params=query_params)
        results = req.json()['results']
        movie_ids = [result.get('id') for result in results][:MAX_RECORDS]


        for movie_id in movie_ids:
            single_movie_url = f"{movie_url}{movie_id}?api_key={TMDb_KEY}"
            req_movie = requests.get(single_movie_url)
            single_movie_result = req_movie.json()
            movie_data = {
                'id' : single_movie_result.get('id',None),
                'adult' : single_movie_result.get('adult',None),
                'budget': single_movie_result.get('budget', None),
                'genres': single_movie_result.get('genres', None),
                'title': single_movie_result.get('title', None),
                'original_title': single_movie_result.get('original_title', None),
                'original_language': single_movie_result.get('original_language', None),
                'overview' : single_movie_result.get('overview', None),
                'popularity': single_movie_result.get('popularity', None),
                'video': single_movie_result.get('video', None),
                'vote_count': single_movie_result.get('vote_count', None),
                'revenue': single_movie_result.get('vote_average', None),
                'runtime': single_movie_result.get('runtime', None),
                'vote_average': single_movie_result.get('vote_average', None),
                'poster_path' : f"https://image.tmdb.org/t/p/original{single_movie_result.get('poster_path',None)}",
                'backdrop_path':  f"https://image.tmdb.org/t/p/original{single_movie_result.get('backdrop_path', None)}",
                'release_date': single_movie_result.get('release_date', None),
            }

            a_movie = {
            'title': movie_data.get('title'),
            'overview': movie_data.get('overview'),
            'release_date': movie_data.get('release_date'),
            'image_url': movie_data.get('backdrop_path'),
            }

            #one_movie = MovieData.objects.create(**a_movie)
            movies_data.append(movie_data)

    context = {
            'movies_data' : movies_data
        }


    return render(request, 'mymovies/home.html', context)


def movie_details(request,id):
    """Returns movie informations
    """
    base_url = f'https://api.themoviedb.org/3/movie/'
    movie_url = f"{base_url}{id}?api_key={TMDb_KEY}"

    req_movie = requests.get(movie_url)
    movie_result = req_movie.json()
    movie_data = {
            'id': movie_result.get('id', None),
            'adult': movie_result.get('adult', None),
            'budget': movie_result.get('budget', None),
            'genres': movie_result.get('genres', None),
            'title': movie_result.get('title', None),
            'original_title': movie_result.get('original_title', None),
            'original_language': movie_result.get('original_language', None),
            'overview': movie_result.get('overview', None),
            'popularity': movie_result.get('popularity', None),
            'video': movie_result.get('video', None),
            'vote_count': movie_result.get('vote_count', None),
            'revenue': movie_result.get('vote_average', None),
            'runtime': movie_result.get('runtime', None),
            'vote_average': movie_result.get('vote_average', None),
            'poster_path': f"https://image.tmdb.org/t/p/original{movie_result.get('poster_path', None)}",
            'backdrop_path': f"https://image.tmdb.org/t/p/original{movie_result.get('backdrop_path', None)}",
            'release_date': movie_result.get('release_date', None),
        }


    context = {
            'movie': movie_data
        }

    return render(request, 'mymovies/detail.html', context)

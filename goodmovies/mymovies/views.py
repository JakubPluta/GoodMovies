import requests
import os
from django.shortcuts import render
from django.http import JsonResponse
from .models import MovieData, WatchList, MovieViewer
import json


TMDb_KEY = os.environ.get('TMDb')



def add_to_watchlist(request):
    data = json.loads(request.body)
    movie_id = data['movie_id']
    user_id = data['user_id']
    action = data['action']
    user = MovieViewer.objects.get(user=user_id)

    watchlist_item = WatchList.objects.create(user=user,
                                                     movie=movie_id)
    watchlist_item.save()


    return JsonResponse('Item was added', safe=False)





def index(request):
    """Main method for searching movies.
    """
    movies_data = []
    if request.method == "POST":
        url = f'https://api.themoviedb.org/3/search/movie?'
        query_params = {
            'query' : request.POST["movie_name"],
            'page' : "1",
            'language' : 'en-US',
            'api_key' : TMDb_KEY
        }
        req = requests.get(url, params=query_params)
        results = req.json()['results']
        for single_movie_result in results:
            movie_data = {
                'id' : single_movie_result.get('id',None),
                'genres': single_movie_result.get('genres', None),
                'title': single_movie_result.get('title', None),
                'overview' : single_movie_result.get('overview', None),
                'popularity': single_movie_result.get('popularity', None),
                'vote_count': single_movie_result.get('vote_count', None),
                'vote_average': single_movie_result.get('vote_average', None),
                'poster_path' : f"https://image.tmdb.org/t/p/original{single_movie_result.get('poster_path',None)}",
                'backdrop_path':  f"https://image.tmdb.org/t/p/original{single_movie_result.get('backdrop_path', None)}",
                'release_date': single_movie_result.get('release_date', None),
            }
            movies_data.append(movie_data)

    context = {
            'movies_data' : movies_data
        }

    return render(request, 'mymovies/home.html', context)





def movie_details(request,id):
    """Returns movie detail informations
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





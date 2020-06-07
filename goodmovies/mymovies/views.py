import requests
import os
from django.shortcuts import render

TMDb_KEY = os.environ.get('TMDb')


def index(request):
    movies_data = []
    MAX_RECORDS = 10

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

            movies_data.append(movie_data)

    context = {
            'movies_data' : movies_data
        }

    #return render(request, 'mymovies/search.html', context)
    return render(request, 'mymovies/home.html', context)

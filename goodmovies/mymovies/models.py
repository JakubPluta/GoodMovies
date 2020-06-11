from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/3.0/ref/models/instances/


class User(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    def __str__(self):
        return self.name


class MovieData(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=5000)
    release_date = models.CharField(max_length=50)
    image_file = models.ImageField(upload_to='images')
    image_url = models.URLField()

    @classmethod
    def create_movie(cls, movie):
        movie = {
            'title' : movie.get('title'),
            'overview': movie.get('overview'),
            'release_date': movie.get('release_date'),
            'image_url': movie.get('backdrop_path'),
        }
        return movie


# class WatchList(models.Model):
#     title = models.CharField(max_length=100)
#     overview = models.TextField(max_length=5000)
#     release_date = models.CharField(max_length=50)
#     image_file = models.ImageField(upload_to='images')
#     image_url = models.URLField()
#     user = models.ForeignKey(User, related_name='add_to_watch',
#                              on_delete=models.CASCADE)
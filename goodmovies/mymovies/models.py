from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# https://docs.djangoproject.com/en/3.0/ref/models/instances/


class MovieViewer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name



class MovieData(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=5000)
    release_date = models.CharField(max_length=50)
    image = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


    @classmethod
    def create_movie(cls, movie):
        movie = {
            'title' : movie.get('title'),
            'overview': movie.get('overview'),
            'release_date': movie.get('release_date'),
            'image_url': movie.get('backdrop_path'),
        }
        return movie





class WatchList(models.Model):
    """WatchList contains Movies saved for given user
    """
    movie = models.SlugField(max_length=255, unique=True, verbose_name='movie')
    #movie = models.CharField(unique=True,max_length=255)
    user = models.ForeignKey(MovieViewer, related_name='add_to_watch',
                             on_delete=models.SET_NULL,null=True)
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)


from django.db import models
from tastypie.resources import ModelResource, ALL, fields
from rental.models import Movie, Genre
from tastypie.authorization import Authorization





# Create your models here.
class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        allowed_methods = ['get','post','patch','put','delete','options']
        authorization = Authorization()




class MovieResource(ModelResource):
    genre = fields.ToOneField(GenreResource, 'genre', full=True)

    class Meta:
        queryset = Movie.objects.all()
        resource_name = "movies"
        ordering = ['title','release_year','price']
        filtering = {
            'release_year': ALL,
            'price':ALL,
            'title':ALL
        }
        allowed_methods = ['get','post','patch','put','delete','options']
        authorization = Authorization()


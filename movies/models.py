from django.db import models

# Create your models here.
class Movie(models.Model): 
    movie_title = models.CharField(max_length=50, null=False)
    movie_genre = models.CharField(max_length=30, null=False)
    movie_director = models.CharField(max_length=60, null=False)
    release_year = models.IntegerField(null=False, default=2000)
    synopsis = models.CharField(max_length=200, null=False) 
    
    def __str__(self) -> str:
        return self.movie_title 
    

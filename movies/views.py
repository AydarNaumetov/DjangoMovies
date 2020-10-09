from django.conf import settings
from django.db import models
from django.db.models import Q, OuterRef, Subquery, Case, When
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Category, Actor, Genre, Rating, Reviews
# from .forms import ReviewForm, RatingForm


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(View):
    """Полное описание"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {"movie": movie})
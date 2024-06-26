from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponse
from django.utils.html import format_html
from . models import CategoryComic, SubCategoryComic, DetailComic
from . models import CategoryMovie, SubCategoryMovie, DetailMovie
from . models import Series, Season, Episode
from . models import Shop, DetailShop
from . models import MarvelHeroes, MarvelVillain, DetailHeroes, DetailVillain
from django.db.models import Q
from itertools import chain
import random
import requests

TMDB_API = 'cd6372556d9c099c35aa482bafbd82cb'

def home(request):
    # Comic Views

    comic = [1, 2, 3, 4, 5, 6]
    comic_spiderman = SubCategoryComic.objects.filter(pk__in=comic)

    comic = [21, 22, 23, 24, 25, 26]
    comic_deadpool = SubCategoryComic.objects.filter(pk__in=comic)

    comic = [16, 17, 18, 19, 20, 21]
    comic_guardians = SubCategoryComic.objects.filter(pk__in=comic)   
    
    shop = list(Shop.objects.all())
    random_shop = random.sample(shop, 12)

    # All Marvel Heroes
    marvel_heroes = MarvelHeroes.objects.all()
    
    # All Marvel Villain
    marvel_villain = MarvelVillain.objects.all()

    return render(request, 'home.html', {'title':"Home", 'marvel_heroes':marvel_heroes, 'marvel_villain':marvel_villain, 'random_shop':random_shop, 'comic_spiderman':comic_spiderman, 'comic_deadpool':comic_deadpool, 'comic_guardians':comic_guardians})

def shop(request):

    shop_1 = Shop.objects.all().order_by('id')[0:12]
    shop_2 = Shop.objects.all().order_by('id')[12:20]

    return render(request, 'shop.html', {'title':"Shop", 'shop_1':shop_1, 'shop_2':shop_2})

def comic(request):
    SC = SubCategoryComic.objects.filter(child=2)
    FF = SubCategoryComic.objects.filter(child=4)
    LATPA = SubCategoryComic.objects.filter(child=1)
    MR = SubCategoryComic.objects.filter(child=6)
    DS = SubCategoryComic.objects.filter(child=7)
    DP = SubCategoryComic.objects.filter(child=3)
    GOTG = SubCategoryComic.objects.filter(child=5)

    items = [1, 6, 11, 16, 21, 30 ]
    feature_comic = SubCategoryComic.objects.filter(pk__in=items)

    items = list(SubCategoryComic.objects.all())
    # change number to how many random items you want
    marvel_comic = random.sample(items, 12)

    return render(request, 'comics.html', {'title':"Comics", 'SC':SC, 'LATPA':LATPA, 'FF':FF, 'MR':MR, 'DP':DP, 'DS':DS, 'GOTG':GOTG, 'feature_comic':feature_comic, 'marvel_comic':marvel_comic})

def movie(request):
    # Movie Views 
    AM = SubCategoryMovie.objects.filter(child=1)
    VU = SubCategoryMovie.objects.filter(child=2)

    # Series Views
    marvel_series = Series.objects.all()

    # All Marvel Heroes
    marvel_movies = SubCategoryMovie.objects.all()

    # Latest Marvel Movies
    videos = (8, 15, 21, 25, 26, 27 )
    latest_movies = SubCategoryMovie.objects.filter(pk__in=videos)

    return render(request, 'movies.html', {'title':"Films", 'marvel_movies':marvel_movies, 'marvel_series':marvel_series, 'latest_movies':latest_movies})

def character(request):
    
    # All Marvel Heroes
    marvel_heroes = MarvelHeroes.objects.all()
    
    # All Marvel Villain
    marvel_villain = MarvelVillain.objects.all()

    return render(request, 'char.html', {'title':"Characters", 'marvel_heroes':marvel_heroes, 'marvel_villain':marvel_villain})

def detail_comics(request, title):
    # Random Comics Views
    items = list(SubCategoryComic.objects.all())
    # change 3 to how many random items you want
    random_items = random.sample(items, 12)

    post = get_object_or_404(SubCategoryComic,title=title)
    detail_comics = DetailComic.objects.filter(post=post)

    return render(request, 'detail_comic.html', {'title':"Comic", 'post':post, 'detail_comics':detail_comics, 'random_items':random_items})

def detail_movies(request, title):
    upload = get_object_or_404(SubCategoryMovie, title=title)
    detail_movies = DetailMovie.objects.filter(upload=upload)
    
    # Random Movies Views
    items = list(SubCategoryMovie.objects.all())
    # change 3 to how many random items you want
    more_movies = random.sample(items, 12)
    
    return render(request, 'detail_movie.html', {'title':"Movie", 'upload':upload, 'detail_movies':detail_movies, 'more_movies':more_movies})

def series(request, title):

    series = get_object_or_404(Series, title=title)

    season = Season.objects.filter(tag_series=series)
    episode = Episode.objects.filter(tag_season__in=season)

    items = list(Series.objects.all())
    # change 3 to how many random items you want
    more_series = random.sample(items, 12)
    
    return render(request, 'series.html', {'series':series, 'more_series':more_series, 'season':season, 'episode':episode})

def detail_series(request, id, tmdb_id, title, season, episode):

    uploads = Episode.objects.filter(id=id)

    items = list(Series.objects.all())
    # change 3 to how many random items you want
    more_series = random.sample(items, 12)

    thumbnail = requests.get(f'https://api.themoviedb.org/3/tv/{tmdb_id}/season/{season}/episode/{episode}/images?api_key={TMDB_API}')

    return render(request, 'detail_series.html', {'uploads':uploads, 'more_series':more_series, 'thumbnail':thumbnail.json() })

def search_films(request):

    if request.method == "GET":
        query = request.GET.get('s')

        if query == '':
            query = 'None'


    search_series = Series.objects.filter(Q(name__icontains=query) | Q(name1__icontains=query) | Q(name2__icontains=query) | Q(name3__icontains=query) | Q(name4__icontains=query) | Q(name5__icontains=query))
    search_movies = SubCategoryMovie.objects.filter(Q(name__icontains=query) | Q(name1__icontains=query) | Q(name2__icontains=query) | Q(name3__icontains=query) | Q(name4__icontains=query) | Q(name5__icontains=query))

    results = chain(search_series, search_movies)
    
    return render(request, 'results_films.html', {'results':results, 'search_series':search_series, 'search_movies':search_movies})

def search_comics(request):

    if request.method == "GET":
        query = request.GET.get('s')

        if query == '':
            query = 'None'


    search_comics = SubCategoryComic.objects.filter(Q(name__icontains=query) | Q(name1__icontains=query) | Q(name2__icontains=query) | Q(name3__icontains=query) | Q(name4__icontains=query) | Q(name5__icontains=query))
    
    return render(request, 'results_comics.html', {'search_comics':search_comics})

def detail_shops(request, title):

    items = get_object_or_404(Shop, title=title)
    detail_shop = DetailShop.objects.filter(items=items)

    shop = list(Shop.objects.all())
    random_shop = random.sample(shop, 8) 

    return render(request, 'detail_shop.html', {'title':"Shop", 'items':items, 'random_shop':random_shop, 'detail_shop':detail_shop})

def detail_heroes(request, title):

    items = get_object_or_404(MarvelHeroes, title=title)
    detail_heroes = DetailHeroes.objects.filter(char_heroes=items)

    return render(request, 'detail_heroes.html', {'title':"Marvel Characters",  'char_heroes':items, 'detail_heroes':detail_heroes})

def detail_villain(request, title):

    items = get_object_or_404(MarvelVillain, title=title)
    detail_villain = DetailVillain.objects.filter(char_villain=items)

    return render(request, 'detail_villain.html', {'title':"Marvel Characters", 'char_villain':items, 'detail_villain':detail_villain})

def about(request):
    return render(request, "about.html",{'title' : "About"})

def admin(request):
    return render(request, "error.html")
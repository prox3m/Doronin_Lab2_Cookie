from django.shortcuts import render, get_object_or_404
from .data import PLANETS, PLANETS_ORDER

def index(request):

    first_slug = PLANETS_ORDER[0]
    return planet_detail(request, first_slug)

def planet_detail(request, slug):

    if slug not in PLANETS:
        return render(request, 'planets/404.html', status=404)
    
    planet = PLANETS[slug]
    menu = [(s, PLANETS[s]['name']) for s in PLANETS_ORDER]

    context = {
        'planet': planet,
        'menu': menu,
        'current_slug': slug,
    }
    
    return render(request, 'planets/planet.html', context)
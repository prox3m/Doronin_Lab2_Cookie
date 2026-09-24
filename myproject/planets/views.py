from django.shortcuts import render, redirect
from django.http import Http404

from .data import PLANETS, PLANETS_ORDER
from .forms import SearchForm

def index(request):
    last = request.COOKIES.get('last_planet')

    if last and last in PLANETS:
        return redirect('planet_detail', slug=last)
    
    return planet_detail(request, PLANETS_ORDER[0])

def planet_detail(request, slug):

    if slug not in PLANETS:
        raise Http404('Планета не наидена')
    
    planet = PLANETS[slug]
    menu = [(s, PLANETS[s]['name']) for s in PLANETS_ORDER]

    context = {
        'planet': planet,
        'menu': menu,
        'current_slug': slug,
    }
    
    response = render(request, 'planets/planet.html', context)

    response.set_cookie('last_planet', slug, max_age = 60 * 60 * 24 * 30)
    
    return response

def search(request):
    form = SearchForm(request.GET)
    results = []
    query = ''

    if form.is_valid():
        query = form.cleaned_data['query'].strip()

        if query:
            query_lower = query.lower()

            for slug in PLANETS_ORDER:
                name = PLANETS[slug]['name']
                
                if query_lower in name.lower():
                    results.append({
                        'slug': slug,
                        'name': name,
                        'description': PLANETS[slug]['description']
                    })
    
    menu = [(s, PLANETS[s]['name']) for s in PLANETS_ORDER]

    context = {
        'form': form,
        'menu': menu,
        'query': query,
        'results': results,
    }

    return render(request, 'planets/search.html', context)
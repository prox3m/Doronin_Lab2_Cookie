from django.shortcuts import render, get_object_or_404
from .data import PLANETS, PLANETS_ORDER
from .forms import SearchForm

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

def search(request):
    """
    Страница поиска. Принимает GET-параметр ?query=..
    Ищет планеты по вхождению подстройки в название.
    """

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
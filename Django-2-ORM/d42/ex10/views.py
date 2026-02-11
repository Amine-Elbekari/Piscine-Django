from django.shortcuts import render
from django.http import HttpResponse
from .models import People, Planets, Movies
from .forms import MoviesMaxReleaseDate, MoviesMinReleaseDate, PlanetDiameterGreaterThen, CharacterGender

# Create your views here.
def display(request):
    results = None
    genders = People.objects.values_list('gender', flat=True).distinct()
    if not genders:
        return HttpResponse("No data availale about gender")
    choices = [(g, g) for g in genders if g]
    if request.method == 'POST':
        gender_drop_down = CharacterGender(request.POST)
        minimum_date = MoviesMinReleaseDate(request.POST)
        maximum_date = MoviesMaxReleaseDate(request.POST)
        planet_diameter_gthen = PlanetDiameterGreaterThen(request.POST)

        gender_drop_down.fields['gender'].choices = choices
        if all([gender_drop_down.is_valid(), minimum_date.is_valid(),
                    maximum_date.is_valid(), planet_diameter_gthen.is_valid()]):
                gender = gender_drop_down.cleaned_data['gender']
                min_date = minimum_date.cleaned_data['min_date']
                max_date = maximum_date.cleaned_data['max_date']
                planet_diameter = planet_diameter_gthen.cleaned_data['planet_diameter']
                results = People.objects.filter(gender=gender,
                    homeworld__diameter__gte=planet_diameter,
                    movies__release_date__range=(min_date, max_date)
                ).values(
                    'name',
                    'gender',
                    'movies__title',
                    'homeworld__name',
                    'homeworld__diameter'
                ).distinct()
    else:
        gender_drop_down = CharacterGender()
        gender_drop_down.fields['gender'].choices = choices
        minimum_date = MoviesMinReleaseDate()
        maximum_date = MoviesMaxReleaseDate()
        planet_diameter_gthen = PlanetDiameterGreaterThen()

    return render(request, 'ex10/display.html', {
        'results': results,
        'gender_form': gender_drop_down,
        'min_form': minimum_date,
        'max_form': maximum_date,
        'diam_form': planet_diameter_gthen,
        'choices': choices
    })


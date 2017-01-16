from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView

from .models import AppleType
from .models import Recipe


# Create your views here.

def apples(request):
    all_apples = AppleType.objects.all()
    context = {'all_apples': all_apples}
    return render(request, 'apple/apple.html', context)


def detail(request, apple_id):
    try:
        apple = AppleType.objects.get(pk=apple_id)
    except AppleType.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, 'apple/detail.html', {'apple': apple})


def index(request):
    context = {}
    return render(request, 'apple/index.html', context)


def recipes(request):
    all_recipes = Recipe.objects.all()
    context = {'all_recipes': all_recipes}
    return render(request, 'apple/recipes.html', context)


class add_apple(CreateView):
    model = AppleType
    fields = ['apple_name', 'ripening_date', 'eating', 'cooking', 'sauce', 'pie', 'juice', 'butter', 'notes']

class add_recipe(CreateView):
    model = Recipe
    fields = ['title', 'apple', 'ingredients', 'steps', 'author', 'picture']

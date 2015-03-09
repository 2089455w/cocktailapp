from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, 'index.html', {})

def cocktail(request):
    return render(request, 'cocktail.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def search(request):
    return render(request, 'search.html', {})
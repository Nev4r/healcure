from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Главная страница
def index(request):
    # Количество посещений
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'index.html', context={'num_visits': num_visits})

def reserve_page(request):
    return render(request, 'reserve.html')
from django.shortcuts import render
import requests

def index(request):
    response = requests.get('http://localhost:8000/api/menu/') 
    menus = response.json()
    return render(request, 'index.html', {'menus': menus})

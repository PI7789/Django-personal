from django.shortcuts import render

import requests

# Create your views here.

def api(request):

    key = "bb399ef9-3a6e-4043-8fd7-b424c19f595f"

    url = f"https://api.openchargemap.io/v3/poi/?key={key}&latitude=53.3093&longitude=-1.1227&maxresults=10"

    response = requests.get(url)
    stations = response.json() if response.status_code == 200 else []

    return render(request, 'pages/api.html', {'stations': stations})
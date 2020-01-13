
# this is my views file
from django.shortcuts import render


# Create your views here.

def home(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=EF02C6A5-A70D-4161-89E4-14F219CFC0B3")
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
      

    return render(request,"home.html", {'api': api})



def about(request):
    return render(request,"about.html", {})
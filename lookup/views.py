
# this is my views file
from django.shortcuts import render


# Create your views here.

def home(request):
    import json
    import requests

    api_key=""
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=" + api_key)
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        
        if api[0]['Category']['Name']  == "Good":
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name']  == "Moderate":
            category_description = "(51-100) Air quality is acceptable, however for some pollutants there may be a moderate health concern for very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Although general pusblic is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "usg"
        elif api[0]['Category']['Name']  == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name']  == "Very Unhealthy":
            category_description = "(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name']  == "Hazerdous":
            category_description = "(301-500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazerdous"
      


        return render(request,"home.html", {'api': api,
            'category_description': category_description, 
            'category_color': category_color})

    else:
        
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=" + api_key)
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        
        if api[0]['Category']['Name']  == "Good":
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name']  == "Moderate":
            category_description = "(51-100) Air quality is acceptable, however for some pollutants there may be a moderate health concern for very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Although general pusblic is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "usg"
        elif api[0]['Category']['Name']  == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name']  == "Very Unhealthy":
            category_description = "(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name']  == "Hazerdous":
            category_description = "(301-500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazerdous"
      


        return render(request,"home.html", {'api': api,
            'category_description': category_description, 
            'category_color': category_color})



def about(request):
    return render(request,"about.html", {})
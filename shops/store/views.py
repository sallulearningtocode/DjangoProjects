from rest_framework.views import APIView
from .models import Shop
from django.shortcuts import render
from math import radians, sin, cos, sqrt, atan2

# Haversine formula to calculate distance between two points
def calculate_distance(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers

        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Calculate differences in latitude and longitude
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Calculate distance using Haversine formula
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance

class IndexView(APIView):
    def get(self, request):
        print("Homepage")
        return render(request,'store/index.html')


class RegisterView(APIView):
    def get(self,request):
            print("GET Register Shop")
            return render(request,"store/registershop.html")
            
    def post(self,request):
            print("POST Register Shop")
            name = request.POST.get('name')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            print(name,latitude,longitude)
            shop = Shop(name=name,latitude=latitude,longitude=longitude)
            shop.save()
            return render(request,"store/registershop.html")

class SearchView(APIView):
    def get(self, request):
        return render(request,'store/search.html')
    
    def post(self,request):  
            print("Search Post Request")
            location = request.POST.get('location')
            latitude,longitude = location.split(',')
            latitude = float(latitude.strip())
            longitude = float(longitude.strip())
            
            print(longitude, latitude)
            shop_details = list(Shop.objects.all().values('name','longitude','latitude'))
            
        
            distances={}
            for shop in shop_details:
                shop_distance = round(calculate_distance(
                latitude, longitude, shop["latitude"], shop["longitude"]
                ),2)
                distances.update({shop["name"]:shop_distance})

            nearest_shops = sorted(distances.items(), key=lambda x: x[1])
            nearest_shops = dict(nearest_shops)
            print(nearest_shops)
            return render(request,'store/search.html',{'shops':nearest_shops})

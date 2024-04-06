from django.shortcuts import render
from rest_framework.views import APIView

class IndexView(APIView):
    def get(self, request):
        print("Homepage")
        return render(request,'store/index.html')

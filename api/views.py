from django.shortcuts import render
from  .models import Hero
from .serializers import HeroSerializer

# Create your views here.
from rest_framework import viewsets

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

    def get_queryset(self):
        name=self.request.query_params.get('name')
        print(name)
        if(name!=None):
            print("params "+name)
            queryset=Hero.objects.filter(name=name)
            return queryset
        else:
            queryset = Hero.objects.all().order_by('name')
            return  queryset





class HeroInformation(viewsets.ModelViewSet):
    queryset = Hero.objects.get(name="satej")
    serializer_class = HeroSerializer
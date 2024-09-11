from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def catalogue(request):
    return render(request,'catalogue.html')


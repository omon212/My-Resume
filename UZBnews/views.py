from django.shortcuts import render
from .models import KunlikNewuz


def index(request):
    return render(request, 'index.html')


# def news(request):
#     return render(request, 'news.html')
#

def news(request):
    news_objects = KunlikNewuz.objects.all()  # Fetch all objects, you can use a filter if needed

    return render(request, 'news.html', {'news_objects': news_objects})


# Create your views here.

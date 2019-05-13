from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'all/pics.html')

def search(request):
  return render(request, 'all/search.html')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#function base view
def home(request):
    return HttpResponse('hello')
    #return render(request, 'home.html', {})
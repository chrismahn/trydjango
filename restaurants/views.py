from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
#function base view
def home(request):
    nums = random.randint(0, 10000)
    return render(request, 'base.html', {'nums': nums})

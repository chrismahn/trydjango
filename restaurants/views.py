from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
#function base view
def home(request):
    nums = random.randint(0, 10000)
    nums2 = random.randint(0, 20000)
    nums3 = random.randint(0, 30000)
    some_list = [nums, nums2, nums3]
    context = {'nums': nums, 'some_list': some_list}
    return render(request, 'base.html', context)

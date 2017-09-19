from django.shortcuts import render
import random
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
#function base view

def home(request):
    nums = random.randint(0, 10000)
    nums2 = random.randint(0, 20000)
    nums3 = random.randint(0, 30000)
    some_list = [nums, nums2, nums3]
    context = {'nums': nums, 'some_list': some_list}
    return render(request, 'home.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

'''
## create  a class based View ##
class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'contact.html', context)
'''

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

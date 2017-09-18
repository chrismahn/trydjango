from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#function base view
def home(request):
    html_ = """<!DOCTYPE html>
    <html lang='eng'>
    <head>
    </head>
    <body>
    <h1>Hello Nurse</h1>
    <p>This is html syntax</p>
    </body>
    </html>
    """
    return HttpResponse(html_)
    #return render(request, 'home.html', {})
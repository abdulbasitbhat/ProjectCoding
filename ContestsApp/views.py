from django.shortcuts import render
from urllib.request import urlopen, Request
import json

# Create your views here.
def index(request):
    #Competitions API
    req = Request(
    url = "https://kontests.net/api/v1/all",
    headers={'User-Agent': 'Mozilla/5.0'}
)   
    #Quotes API
    req1 = Request(
    url = "https://api.quotable.io/quotes/random?tags=competition",
    headers={'User-Agent': 'Mozilla/5.0'}
)
    
    response = urlopen(req)
    json_data = json.loads(response.read())
   
    response1 = urlopen(req1)
    json_data1 = json.loads(response1.read())
    context = {
        'data':json_data,
        'data1':json_data1[0],
    }

    return render(request,'index.html',context)
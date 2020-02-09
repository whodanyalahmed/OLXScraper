from django.shortcuts import render
from django.views.generic import TemplateView

import requests
from bs4 import BeautifulSoup
# Create your views here.


class homeView(TemplateView):
    template_name = "index.html"



def search(request):
    url = request.POST["url"]
    # url = request.POST.get('url',None)
    # con = Person.objects.get(name = url)
    html = requests.get("https://www.olx.com.pk/items/q-"+url)
    soup = BeautifulSoup(html.text,"lxml")
    name =  []

    for each_name in soup.findAll('span',{'class': '_2tW1I'}):
        mname = each_name.text
        # print(mname)
        name.append(mname)

    price = []
    for each_price in soup.findAll('span',{'class':'_89yzn'}):
        mprice = each_price.text
        sprice = mprice.split()
        co = sprice[1].replace(",","")
        # print(co)
        price.append(co)
        
    dt = dict(zip(name,price))
    # print(dt)
    # print(dt)
    price = 0
    minprice = minpr(price)
    minname = ""
    for k,v in dt.items():
        if int(v) < minprice:
            minprice = int(v)
            minname = k
    return render(request,"search.html",context={'html':html,'min_name':minname,'min_price':minprice})


def minpr(d):
    if d == 0:
        return 100000000000000000000
    else:
        return 1 
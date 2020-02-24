from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,StreamingHttpResponse,FileResponse
import requests,os
from django.conf import settings
from django.core.files import File
from bs4 import BeautifulSoup
# Create your views here.


class homeView(TemplateView):
    template_name = "index.html"

class minView(TemplateView):
    template_name = "min.html"

class maxView(TemplateView):
    template_name = "max.html"


class listView(TemplateView):
    template_name = "list.html"


def search(request):
    url = request.POST["url"]
    title = request.POST.get('title')
    # url = request.POST.get('url',None)
    # con = Person.objects.get(name = url)
    try:    
        html = requests.get("https://www.olx.com.pk/items/q-"+url)
        scode = html.status_code
        # print(html.status_code)

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
        link = []
        for each_img in soup.findAll('img',{'class':'_3Kg_w'}):
            mlink = each_img['src']
            link.append(mlink)
            # print(mlink)
        dt = dict(zip(name,price))
        # print(dt)
        # print(dt)
        price = 0
        mincount = 0
        maxcount = 0
        minprice = minpr(price)
        maxprice = 0
        minname = ""
        maxname = ""
        for k,v in dt.items():
            if int(v) < minprice:
                minprice = int(v)
                minname = k
                mincount +=1

        for k,v in dt.items():
            if int(v) > maxprice:
                maxprice = int(v)
                maxname = k
                maxcount +=1

        minsrc = link[mincount]
        maxsrc = link[maxcount]
        return render(request,"search.html",context={'title':title,'html':html,'min_name':minname,'min_price':minprice,'max_name':maxname,'max_price':maxprice,'minsrc':minsrc,'maxsrc':maxsrc})
    except Exception as e:
        return render(request,"notfound.html",{'error':e})

pathtofile = settings.STATIC_ROOT+"\\files\\names.csv"
file_name = "names.csv"
# def downView(request):
#   #get the filename of desired excel file
#     path_to_file = pathtofile #get the path of desired excel file
#     response = HttpResponse()
#     response['Content-Disposition'] = 'attachment; filename=%s' % file_name
#     response['X-Sendfile'] = path_to_file
#     return response
#     # return render(request,"download.html",context={'path':pathtofile})


def downView(request):
    f = open(pathtofile, "r")
    response = FileResponse(f, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=names.csv'
    response['X-Sendfile'] = pathtofile
    f.close()
    return response

def test(request):
    title = request.POST.get('title')
    return HttpResponse(title)

def listextract(request):
    url = request.POST["url"]
    title = request.POST.get('title')
    # url = request.POST.get('url',None)
    # con = Person.objects.get(name = url)
    try:    
        html = requests.get("https://www.olx.com.pk/items/q-"+url)
        scode = html.status_code
        # print(html.status_code)

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
        link = []
        for each_img in soup.findAll('img',{'class':'_3Kg_w'}):
            mlink = each_img['src']
            link.append(mlink)
            # print(mlink)
        dt = dict(zip(name,price))
        path = settings.STATIC_ROOT+"\\files"
        try:
            os.chdir(path)
            print("File is already there")
            pass
        except Exception as f:
            os.mkdir(path)
            print("File created")
        print(path)
        print(pathtofile)
        header = "name,price\n"
        with open(pathtofile,"w+") as f:
            myfile = File(f)
            myfile.write(header)
            for k,v in dt.items():
                k = k.replace("," , "-")
                myfile.write(k + "," + v + "\n")
        return render(request,"search.html",context={'title':title,'html':html,'path':pathtofile})
    except Exception as e:
        return render(request,"notfound.html",{'error':e})

def minpr(d):
    if d == 0:
        return 100000000000000000000
    else:
        return 1 
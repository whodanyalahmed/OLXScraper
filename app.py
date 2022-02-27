import requests
from bs4 import BeautifulSoup


def minpr(d):
    if d == 0:
        return 100000000000000000000
    else:
        return 1


price = 0
mincount = 0
maxcount = 0
minprice = minpr(price)
maxprice = 0
minname = ""
maxname = ""
# url = request.POST.get('url',None)
# con = Person.objects.get(name = url)
url = "iphone-7"
try:
    html = requests.get("https://www.olx.com.pk/items/q-"+url)
    scode = html.status_code
    print(html.status_code)

    soup = BeautifulSoup(html.text, "lxml")

    price = []
    name = []
    link = []
    # get all the UL tags
    for ul in soup.findAll('ul', {'class': 'ba608fb8'}):
        # get all the LI tags
        for li in ul.findAll('li'):
            # print(li)
            # get the text
            # mname = li
            # get the div in li with attribute aria-label="Title"
            for name_div in li.findAll('div', {'aria-label': 'Title'}):
                print(name_div.text)
                name.append(name_div.text)
            for price_div in li.findAll('div', {'aria-label': "Price"}):
                print(price_div.text)
                mprice = price_div.text
                sprice = mprice.split()
                co = sprice[1].replace(",", "")
                price.append(co)
            # get the image attribute data-src
            try:

                img = li.find('img')
                print(img['src'])
                link.append(img['src'])
            except Exception as e:
                print('exception', e)
    print("this is after loop")
    # for each_name in soup.findAll('span', {'class': '_2tW1I'}):
    #     mname = each_name.text
    #     # print(mname)
    #     name.append(mname)

    # for each_price in soup.findAll('span', {'class': '_89yzn'}):
    #     mprice = each_price.text
    #     sprice = mprice.split()
    #     co = sprice[1].replace(",", "")
    #     # print(co)
    #     price.append(co)
    # for each_img in soup.findAll('img', {'class': '_3Kg_w'}):
    #     mlink = each_img['src']
    #     link.append(mlink)
    #     print(mlink)
    print(len(name))
    print(len(price))
    print(len(link))
    dt = dict(zip(name, price))
    # print(dt)
    # print(dt)

    for k, v in dt.items():
        if int(v) < minprice:
            minprice = int(v)
            minname = k
            mincount += 1

    for k, v in dt.items():
        if int(v) > maxprice:
            maxprice = int(v)
            maxname = k
            maxcount += 1

    try:
        minsrc = link[mincount]
        maxsrc = link[maxcount]

        print("try: " + minsrc + " " + str(mincount))
        print(maxsrc + " " + str(maxcount))
    except Exception as e:
        print("except: " + str(e))
except Exception as e:
    print("error: Something went wrong or "+str(e))

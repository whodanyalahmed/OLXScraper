from urllib.request import urlopen
html = urlopen("https://www.olx.com.pk").read()


print(html)
import requests
from bs4 import BeautifulSoup
def getdata(url):
    r=requests.get(url)
    return r.text
htmldata=getdata("https://covid-19tracker.milkeninstitute.org/")
soup=BeautifulSoup(htmldata, 'html.parser')
res=str(soup.find_all("div",class_="is_h5-2 is_developer w-richtext"))
print("NO 1 " + res[46:86])
print("NO 2 " + res[139:218])
print("NO 3 " + res[279:299])
print("NO 4 " + res[300:320])
print("NO 5 " + res[415:500])


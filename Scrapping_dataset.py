from bs4 import BeautifulSoup as bs
import requests
from newspaper import Article
import csv
import pandas as pd

#list_cat=['sport','politique','economie','art-et-culture']
list_cat=['art-et-culture']
list_cat_desc={}
i=0
def get_Article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
    except:
        print('url not found')
    return article.text


def getCatLine(cat):
    carlisturl=[]
    for i in range(1,50):
        url='https://www.hespress.com/'+cat+'/index.'+str(i)+'.html'
        print(url)
        r = requests.get(url)
        soup = bs(r.content, 'lxml')
        links = [item['href'] if item.get('href') is not None else item['src'] for item in soup.select('a') ]
        for l in links:
            if "/"+cat+"/" in l and "index" not in l :
                carlisturl.append(l)
    carlisturl = list(dict.fromkeys(carlisturl))
    return carlisturl

for cat in list_cat:
   carlisturl = getCatLine(cat)
   with open('hyspress_dataset.csv', 'a', newline='',encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for listliencategory in carlisturl:
            url=str("https://www.hespress.com"+listliencategory)
            print(url)
            article=get_Article(url)
            if article:
                article=article.replace("\n"," ")
                spamwriter.writerow([cat,article])
                i=i+1
                print(i)











    



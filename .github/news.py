import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

titleList=[]
for k in range(1,100,10):
    res=req.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%86%8D%EB%B3%B4&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=35&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:all,a:all&start="+str(k))
    soup=bs(res.text,"lxml")
    title=soup.select("a.news_tit")
    for i in title:
        titleList.append(i.text)
titletu= tuple(titleList)
dic = {"뉴스제목": titletu}
df = pd.DataFrame(dic)
df.to_csv("data.csv",encoding="UTF-8",index=False)

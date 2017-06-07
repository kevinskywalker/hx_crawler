# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:10:49 2017

@author: liujiacheng1
"""



import requests as req
import  bs4


"""
warning:
hx_tougu
hx_attention
hx_gegu
hx_yanbao
"""


def hx_crawl():
    
    url = 'http://www.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'newsList'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
  
    
def hx_news():
    
    url = 'http://news.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'m_news'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
def hx_event():
    
    url = 'http://news.hexun.com/events/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'w_620'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
    
def hx_stock():
    
    url = 'http://stock.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'newsList'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
def hx_yanbao():
    
    url = 'http://yanbao.stock.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'yb_list03'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    

    print(final)
    
    

    
    
    
def hx_opinion():
    
    url = 'http://opinion.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'style':'display:none;'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
def hx_mingjia():
    
    url = 'http://news.hexun.com/socialmedia/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'newsTitle'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
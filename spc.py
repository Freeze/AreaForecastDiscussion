#!/usr/bin/env python

from pyiem.nws.products.spcpts import parser
import requests
from bs4 import BeautifulSoup

def get_latest_outlook():
#    Pretend you never saw this.  
#    page = requests.get("https://www.spc.noaa.gov/products/outlook/day1otlk.html")
#    soup = BeautifulSoup(page.text, "lxml")
#    link = soup.find('a', text="WUUS01 PTSDY1")
#    full_link = "https://www.spc.noaa.gov%s" % (link['href'])
    pts_list = requests.get("https://api.weather.gov/products/types/pts")
    latest = pts_list.json()['@graph'][0]['@id']
    latest_text = requests.get(latest).json()['productText']
    return latest_text

latest = get_latest_outlook()
prod = parser(latest)
prod.draw_outlooks()




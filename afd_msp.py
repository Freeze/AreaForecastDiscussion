#!/usr/bin/env python
import requests

url = "https://api.weather.gov/products/types/afd/locations/mpx"

headers = {
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.weather.gov",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

latest_afd = response.json()['@graph'][0]['@id']

afd_txt = requests.request("GET", latest_afd, headers=headers)

afd_json = afd_txt.json()

print(afd_json['issuanceTime'])
print(afd_json['productText'])

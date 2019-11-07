# -*- coding: utf-8 -*-
import requests
import json
import scrapy
from ..items import DevtoScraperItem
import csv
from devto_scraper import settings
# Get the users


API_KEY = "b08489876db89d500d55b6dd309e527b"

class DevtoSpiderSpider(scrapy.Spider):
    name = 'devto_spider'
    comp_criteria = "Mount Allison University"
    # comp_criteria = "I'm looking for work"
    #allowed_domains = ['dev.to/fidelve']
    API_URL = "http://api.scraperapi.com/?api_key=%s&url=" % API_KEY
    base_url = 'https://dev.to/'

    paths = []

    def start_requests(self):
        #Getting all user's profile link
        request_url = "https://ye5y9r600c-dsn.algolia.net/1/indexes/ordered_articles_production/query"
        querystring = {"x-algolia-agent": "Algolia for vanilla JavaScript 3.20.3",
                       "x-algolia-application-id": "YE5Y9R600C",
                       "x-algolia-api-key": "YWVlZGM3YWI4NDg3Mjk1MzJmMjcwNDVjMjIwN2ZmZTQ4YTkxOGE0YTkwMzhiZTQzNmM0ZGFmYTE3ZTI1ZDFhNXJlc3RyaWN0SW5kaWNlcz1zZWFyY2hhYmxlc19wcm9kdWN0aW9uJTJDVGFnX3Byb2R1Y3Rpb24lMkNvcmRlcmVkX2FydGljbGVzX3Byb2R1Y3Rpb24lMkNDbGFzc2lmaWVkTGlzdGluZ19wcm9kdWN0aW9uJTJDb3JkZXJlZF9hcnRpY2xlc19ieV9wdWJsaXNoZWRfYXRfcHJvZHVjdGlvbiUyQ29yZGVyZWRfYXJ0aWNsZXNfYnlfcG9zaXRpdmVfcmVhY3Rpb25zX2NvdW50X3Byb2R1Y3Rpb24lMkNvcmRlcmVkX2NvbW1lbnRzX3Byb2R1Y3Rpb24="}
        headers = {
            'accept': "application/json",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            'content-type': "application/json",
            'sec-fetch-mode': "cors",
            'cache-control': "no-cache"
        }

        pagenum = 0
        perpage = 15
        # perpage = 260000

        # Repeating part while people is none
        payload = "{\"params\":\"query=*&hitsPerPage="+str(perpage)+"&page="+str(pagenum)+"&attributesToHighlight=%5B%5D&tagFilters=%5B%5D\"}"
        response = requests.request("POST", request_url, data=payload, headers=headers, params=querystring)
        json_obj = json.loads(response.text)
        for i in range(perpage):
            path = json_obj['hits'][i]['user']['username']
            tmp_path = self.API_URL + self.base_url + path
            self.paths.append(tmp_path)

        # print("paths:", self.paths)
        for url in self.paths:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        item = DevtoScraperItem()
        # print("username:", username.encode('utf-8').decode('iso-8859-9'))
        # print("username:", username.encode().decode('utf8'))
        # print("profile path: ", response.request.url.split("url=")[1])

        values = response.xpath('//div[@class="value"]/text()')
        # username = response.xpath('//span[@itemprop="name"]/text()').extract()[0]
        # profile_path = response.request.url.split("url=")[1]
        # item['name'] = username.encode('utf-8').decode('iso-8859-9')
        # item['path'] = profile_path
        # yield item

        for value in values:
            tmp_val = value.extract().strip()

            if tmp_val == self.comp_criteria:
                username = response.xpath('//span[@itemprop="name"]/text()').extract()[0]
                profile_path = response.request.url.split("url=")[1]
                item['name'] = username.encode('utf-8').decode('iso-8859-9')
                item['path'] = profile_path
                yield item
        # pass
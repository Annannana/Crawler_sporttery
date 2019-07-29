# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import json
from sporttery.items import SportteryItem

class LotterySpider(scrapy.Spider):
    name = 'lottery'
    allowed_domains = ['yuntuapi.amap.com']
    base_url = 'https://yuntuapi.amap.com/datasearch/local?s=rsv3&key=b8b352fbcb16290ed546402a6bb141c3&extensions=base&enc=utf-8&keywords=&sortrule=_id:1&tableid=550a9255e4b005aa558a4006&'

    def start_requests(self):
        province = ['北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省',
                    '山东省', '河南省',
                    '湖北省', '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区',
                    '西藏自治区',
                    '宁夏回族自治区', '新疆维吾尔自治区', '香港特别行政区', '澳门特别行政区']
        for city in province:
            params = {
                'limit': 100,
                'page': 1,
                'city': city
            }
            yield scrapy.Request(url=self.base_url + urlencode(params), callback=self.parse,
                                 meta={"info": params})
    def parse(self, response):
        info = response.meta.get("info")
        page = info['page']
        city = info['city']
        rsp = json.loads(response.text)
        if page == 1:
            count = int(rsp['count'])
            total_page = (count + 99) // 100
            for i in range(2, total_page + 1):
                params = {
                    'limit': 100,
                    'page': i,
                    'city': city
                }
                yield scrapy.Request(url=self.base_url + urlencode(params), callback=self.parse,
                                     meta={"info": params})

        datas = rsp['datas']
        for data in datas:
            item = SportteryItem()
            item['MapType'] = 1
            item['phone'] = [(data['tel'])]
            item['city'] = data['city']
            item['province'] = data['province']
            item['address'] = data['_address']
            item['lat'] = data['x']
            item['lng'] = data['y']
            item['mainname'] = "体育彩票"
            item['topic'] = ["体育彩票"]
            item['tag'] = ["体育彩票"]
            item['name'] = "体育彩票(" + data['_id'] + ")"
            item['officialurl'] = 'https://www.sporttery.cn'
            item['microblog'] = 'https://www.weibo.com/p/1002063072038031'
            item['category'] = ['彩票点']
            yield item

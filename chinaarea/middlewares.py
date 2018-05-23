# # -*- coding: utf-8 -*-
#
# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#
# from scrapy import signals
#
#
# class ChinaareaSpiderMiddleware(object):
#

import random

# class UserAgentMiddleware(object):
#     """
#     给每个请求随机切换一个USER_AGENT
#     """
#     def process_request(self,request, spider):
#         user_agent = random.choice(ua_list)
#         request.headers['User-Agent'] = user_agent
#         # request.meta['proxy']

from selenium import webdriver
import time
import scrapy

from chinaarea.settings import USER_AGENTS as ua_list
# import random
# # class UserAgentMiddleware(object):
#     """
#     给每个请求随机选取user_Agent
#     """
#     # def process_request(self,request, spider):
#     #     user_agent = random.choice(ua_list)
#     #     request.headers['USER_AGENTS'] = user_agent
#     #     # request.meta['proxy']  设置代理
#     #     print('request: ', request.headers['USER_AGENTS'] )
#     #     print('*'*30)

from selenium import webdriver
import time
import scrapy

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        self.driver = webdriver.Chrome()
        if request.url != "https://www.aqistudy.cn/historydata/":
            self.driver.get(request.url)
            time.sleep(2)
            html = self.driver.page_source
            self.driver.quit()
            return scrapy.http.HtmlResponse(url=request.url, body=html, encoding="utf-8", request=request)

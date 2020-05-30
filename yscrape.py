#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import psycopg2
import re
import io
import six
import codecs
from datetime import timedelta
import time
import datetime
import argparse
import json
#import scrape_d
#import scrape_b
#import sentimentj
import scrapeyahoo
import scraperss
import  scrapeyahoous
#import scrapesankei

main='00000200'

#nikkei
'''
ptno='00000018'
url="https://assets.wor.jp/rss/rdf/nikkei/business.rdf"
wtype='nikkei'  
scraperss.scrrss(ptno,url,wtype,main)
#

ptno='00000017'
url="https://assets.wor.jp/rss/rdf/nikkei/news.rdf"
wtype='nikkei'  
scraperss.scrrss(ptno,url,wtype,main)
ptno='00000019'
url="https://assets.wor.jp/rss/rdf/nikkei/economy.rdf"
wtype='nikkei'  
scraperss.scrrss(ptno,url,wtype,main)
#bl
ptno='00000030'
url="https://assets.wor.jp/rss/rdf/bloomberg/top.rdf"
wtype='b'  
scraperss.scrrss(ptno,url,wtype,main)
ptno='00000030'
url="https://assets.wor.jp/rss/rdf/bloomberg/markets.rdf"
wtype='b'  
scraperss.scrrss(ptno,url,wtype,main)
ptno='00000031'
url="https://assets.wor.jp/rss/rdf/bloomberg/overseas.rdf"
wtype='b'  
scraperss.scrrss(ptno,url,wtype,main)
#routers


ptno='00000111'
url="https://assets.wor.jp/rss/rdf/reuters/business.rdf"
wtype='routers'  
scraperss.scrrss(ptno,url,wtype,main)
ptno='00000110'
url="https://assets.wor.jp/rss/rdf/reuters/top.rdf"
wtype='routers'  

scraperss.scrrss(ptno,url,wtype,main)
#yahoo
'''
'''
ptno='00000021'
url="https://news.yahoo.co.jp/ranking/access/news"
wtype='y'
scrapeyahoo.scrrss2(ptno,url,wtype,main)
ptno='00000022'
url="https://news.yahoo.co.jp/categories/business"
wtype='y'
scrapeyahoo.scrrss2(ptno,url,wtype,main)
'''
yurl='https://news.yahoo.com/us'
scrapeyahoous.scrrss2('00000220','nsnote','https://news.yahoo.com/us','yahoo')

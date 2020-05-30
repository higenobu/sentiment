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
#import scrapeyahoo
import scraperss3
#import  scrapeyahoous
#import scrapesankei

main='00000200'

#nikkei
ptno='00000018'
url="https://assets.wor.jp/rss/rdf/nikkei/business.rdf"
wtype='nikkei'  
scraperss3.scrrss3(ptno,url,wtype,main)
#

ptno='00000017'
url="https://assets.wor.jp/rss/rdf/nikkei/news.rdf"
wtype='nikkei'  
scraperss3.scrrss3(ptno,url,wtype,main)
ptno='00000019'
url="https://assets.wor.jp/rss/rdf/nikkei/economy.rdf"
wtype='nikkei'  
scraperss3.scrrss3(ptno,url,wtype,main)
#bl
ptno='00000030'
url="https://assets.wor.jp/rss/rdf/bloomberg/top.rdf"
wtype='b'  
scraperss3.scrrss3(ptno,url,wtype,main)
ptno='00000030'
url="https://assets.wor.jp/rss/rdf/bloomberg/markets.rdf"
wtype='b'  
scraperss3.scrrss3(ptno,url,wtype,main)
ptno='00000031'
url="https://assets.wor.jp/rss/rdf/bloomberg/overseas.rdf"
wtype='b'  
scraperss3.scrrss3(ptno,"https://assets.wor.jp/rss/rdf/bloomberg/overseas.rdf",wtype,main)
#routers


ptno='00000111'
url="https://assets.wor.jp/rss/rdf/reuters/business.rdf"
wtype='routers'  
scraperss3.scrrss3(ptno,url,wtype,main)
ptno='00000110'
url="https://assets.wor.jp/rss/rdf/reuters/top.rdf"
wtype='routers'  

scraperss3.scrrss3(ptno,url,wtype,main)

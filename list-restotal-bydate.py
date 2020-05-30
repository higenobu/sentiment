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
import sys
import csv
#select seq,sum(predict::int) from res where predict='1' group by seq order by seq;
#select seq,cont,sum(predict::int) from res where predict='1' group by seq,cont order by seq;
#select resdate,seq,cont,sum(predict::int) from res where predict='1' group by seq,cont,resdate order by seq;
def sel_date():
  dbname='news'
  #use news for news server
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:    
    sql1="select resdate from res "
    sql2=" order by resdate desc limit 1"    
    sql =sql1+sql2
    print (sql)
    cur.execute(sql)
    rows = cur.fetchall()  
    return rows
  except (Exception, psycopg2.DatabaseError) as error:

    pass
  finally:
    if conn is not None:
      conn.close()
#*****************************************
def sel_news(filenm,ddate):
  dbname='news'
  #use news for news server
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  if (ddate==''):
    ddate=tdate
  print ("sel date",ddate)
  
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    
    sql1="select count(predict),predict,filenm from res where "
    sql2="resdate="+"'"+ddate+"'"+ " and filenm like "+"'%"+filenm+"%'"
    sql3= " group by predict,filenm"

    sql =sql1+sql2+sql3
    print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    return rows
  except (Exception, psycopg2.DatabaseError) as error:

    pass
  finally:
    if conn is not None:
      conn.close()
#********************************
#main**************
args = sys.argv
target=args[1]
now=datetime.datetime.now()
tdate=now.strftime("%Y-%m-%d")
#wdates=sel_date()
ddate=args[3]

'''
if (len(wdates)>0):
  wdate=wdates[0][0]
  ddate=str(wdate)
  print (ddate)
else:
  print (tdate)
  ddate=tdate
'''

ff=open(target,'r')
news=ff.readline()
nw=[]
while (news):
  news=news.strip()
  nw.append(news)
  news=ff.readline()
    
  print (news)

with open(args[2], 'w') as f:
  maxval=0
  maxtag='-'
  prenn=''
  jj=0
  for nn in nw:
    print (nn)
    '''
    if (nn==''):
      cont=str(maxval)+','+maxtag+','+'***********************'+prenn+'\n'
      f.write(cont)
      continue
    '''



    #res=sel_news(ffname,ddate)
    msg=''
    pp=prenn.find("2chi")
    #2020-05-10 see find return 
    if(pp>0):
      if (maxtag=='0'):
        msg="Down"
      elif (maxtag=='1'):
        msg='Up'
      else:
        msg='-'

    else:
      if (maxtag=='1'):
        msg="Down"
      elif (maxtag=='2'):
        msg="Up"
      else:
        msg="-"
        
    if (jj>0):
      
      cont=str(maxval)+','+maxtag+','+'***'+msg+'****'+ddate+'****'+str(float(maxval/jj))+'**********'+prenn+'\n'
      f.write(cont)

    data=[]
    maxval=0
    prenn=nn
    if (nn==''):
      print ("No more")
      continue
    ffname='/tmp/'+nn
    res=sel_news(ffname,ddate)
    if (res):
      pass
    else:
      continue
    jj=0
    for rr in res:

      if (rr in data):
        continue
      else:
        jj+=rr[0]
        data.append(rr)

      cont=str(rr[0])+','+rr[1]+','+rr[2]+'\n'
      if (maxval<rr[0]):
        maxval=rr[0]
        maxtag=rr[1]

      print (cont)
      f.write(cont)
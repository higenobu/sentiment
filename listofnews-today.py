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
def sel_news_file(filenm):
  with open(filenm) as g:
    reader = csv.reader(g, delimiter=',')
    lg = [row for row in reader]
    
    news=[]
    newstag=[]
    ii=0
    for m in lg:
        newstag.append(m[2])
        news.append(m[4])
        #print (m[1])
        ii+=1
    print ("news-res:",ii)
  
    return lg

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
tdate=now.strftime("%Y%m%d")
yes=now + timedelta(days=-1)
ydate=yes.strftime("%Y%m%d")
#wdates=sel_date()
#ddate=args[3]
#print (ddate)

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
if (args[3]=='y'):
  writefile=args[2]+ydate+'.csv'
  ddate=ydate
else:
  ddate=tdate
  writefile=args[2]+tdate+'.csv'

print (writefile)
with open(writefile, 'w') as f:
  maxval=0
  maxtag='-'
  msg=''
  jj=0
  for nn in nw:
    print (nn)    
    data=[]
    maxval=0
    
    if (nn==''):
      print ("No more")
      continue
    ffname='/tmp/'+nn+'_'+ddate+'.csv'
    print (ffname) 
    if (os.path.isfile(ffname)):
      exist=True      
      print (ffname)
  
    else:
      print ("NO resfile")
      exist=False
    if (exist):
      pass
    else:
      continue
    res=sel_news_file(ffname)
    if (res):
      pass
    else:
      continue
    jj=0
    down=0
    up=0
    nu=0

    for rr in res:

      jj+=1

      cont=str(rr[2])+','+rr[4]+'\n'
      print (cont)

      if (rr[2]=='1'):
          down+=1
      elif (rr[2]=='2'):
          up+=1
      elif (rr[2]=='0'):
          nu+=1
    print (down,up,nu)
    if (down<up):
      if (nu<up):
        maxval=up
        maxtag='2'
      else:
        maxval=nu

    elif (up<down):
      if (nu<down):
        maxval=down
        maxtag='1'
      else:
        maxval=nu
        maxtag='0'
    else:
      if (up<nu):
          maxval=nu
          maxtag='0'
      else:
          maxval=up
          maxtag='1'
    print (maxval/jj)
    cont='Down:1,'+str(down)+',Up:2,'+str(up)+',Nutral:0,'+str(nu)+',Total,'+str(jj)+',Date,'+ddate+',File,'+ffname+'\n'
    f.write(cont)
    cont=str(maxval)+','+maxtag+','+str(jj)+','+ddate+','+str(maxval/jj)+','+ffname+'\n'
    f.write(cont)


        

     
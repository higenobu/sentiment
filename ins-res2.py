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
def sel_news(cont,filenm):
  dbname='news'
  #use news for news server
  now=datetime.datetime.now()
  nextdate=now + timedelta(days=1)
  tdate=now.strftime("%Y-%m-%d")
  ndate=nextdate.strftime("%Y-%m-%d")
  wfilenm='%'+filenm+'%'
  if (len(cont)>50):
    subcont='%'+cont[1:50]+'%'
  else:
    subcont='%'+cont[1:]+'%'
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select id from res where '
    where='  filenm like '+"'"+wfilenm+"'"+" and resdate="+"'"+ndate+"'"
    print (sql+where)
    cur.execute(sql+where)

    rows = cur.fetchall()
    if (len(rows)>0):
      return True
    else:
      return False
  except (Exception, psycopg2.DatabaseError) as error:

    pass
  finally:
    if conn is not None:
      conn.close()

def ins_res(row,filenm):
  dbname='news'
  #use news for news server
  #insert use nextdate
  #2020-5-17 updated

  now=datetime.datetime.now()
  nextdate=now + timedelta(days=1)
  tdate=now.strftime("%Y-%m-%d")
  ndate=nextdate.strftime("%Y-%m-%d")
  strnow=now.strftime("%Y-%m-%d %H:%M:%S")
  #print (nextdate)
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  aa=row[0]
  bb=row[1]
  cc=row[2]
  dd=row[3]
  if (aa=='seq-no'):
    return

  #bb = unicode(bb, errors='ignore')
  #encode='utf-8'
  #cur.execute("set client_encoding to '%s'" % encode)
  try:
    sql = """INSERT INTO res(resdate,seq,fixed,predict,filenm,cont,proctime) 
    VALUES(%s,%s,%s,%s,%s,%s,%s) """
    cur.execute(sql, (ndate,aa,bb,cc,filenm,dd,strnow))
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    print ("ERROR INS")
    pass
  finally:
    if conn is not None:
      conn.close()
  return 

args = sys.argv
fname=args[1]
aa=fname.find("_")
if (aa):
  filenm=fname[0:aa]
else:
  filenm=fname[:]


with open(args[1]) as f:
    reader = csv.reader(f, delimiter=',')
    ls = [row for row in reader]

    result_rows = []
    ii=0
    ww=ls[1]
    print (ww)
    new=False
    if (sel_news(ww[4],filenm)):
      new=False
      print ("res exist")
    else:
      new=True
      for i in range(len(ls)):
        if (len(ls[i])>1 and i<(len(ls)-1)):

          if (ls[i][0]=='seq-no'):
            continue
        
          ii+=1
          result_rows.append([ ls[i][0],ls[i][1],ls[i][2],ls[i][4]])
      print (ii)

if (new):
  for k in range(len(result_rows)):
    ins_res(result_rows[k],filenm)
  
with open(args[2], 'w') as f:
  if (new):
    writer = csv.writer(f, delimiter=',')
    writer.writerows(result_rows)

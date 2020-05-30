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

def ins_res(row,filenm):
  dbname='news'
  #use news for news server
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  strnow=now.strftime("%Y-%m-%d %H:%M:%S")
  #print ("INS")
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
    cur.execute(sql, (tdate,aa,bb,cc,filenm,dd,strnow))
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    print ("ERROR INS")
    pass
  finally:
    if conn is not None:
      conn.close()
  return 



#import mojimoji

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
    for i in range(len(ls)):
        if (len(ls[i])>1 and i<(len(ls)-1)):
          if (ls[i][0]=='seq-no'):
            continue
        
          ii+=1
          result_rows.append([ ls[i][0],ls[i][1],ls[i][2],ls[i][4]])
    print (ii)

for k in range(len(result_rows)):
  #print (result_rows[k])

  ins_res(result_rows[k],filenm)

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(result_rows)

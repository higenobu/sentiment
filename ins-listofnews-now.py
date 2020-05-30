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
def ins_listofnews(tdate,total,down,up,nu,maxval,maxtag,filenm):
  #print(read_config()['database'])
  dbname='news'
  
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  #tdate=yes.strftime("%Y-%m-%d")
  #tdate=now.strftime("%Y-%m-%d")  
  stotal=str(total)
  sdown=str(down)
  sup=str(up)
  snu=str(nu)
  smaxval=str(maxval)
 

  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    
    sql = """INSERT INTO listofnews(tdate,total,down,up,nu,maxval,maxtag,filenm)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s) """
    cur.execute(sql, (tdate,stotal,sdown,sup,snu,smaxval,maxtag,filenm))
    conn.commit()
    
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    pass
  finally:
    if conn is not None:
      conn.close()
  return

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
ff=open(target,'r')
news=ff.readline()
nw=[]
while (news):
  news=news.strip()
  nw.append(news)
  news=ff.readline()
    
  print (news)
now=datetime.datetime.now()
todaydate=now.strftime("%Y%m%d")
now=datetime.datetime.now()
jj=0

writefile=args[2]+todaydate+'.csv'
print (writefile)
with open(writefile, 'w') as f:
  if (1):
    nextdate=now + timedelta(days=1)
    tdate=nextdate.strftime("%Y%m%d")
    print ("news date:",tdate)




    maxval=0
    maxtag='-'
    msg=''
    jj=0
    for nn in nw:
      #print (nn)    
      data=[]
      maxval=0
    
      if (nn==''):
        print ("No more")
        continue
      ffname='/tmp/'+nn+'_'+tdate+'.csv'
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
        #print (cont)

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
      #print (maxval/jj)
      cont='1(down for 3chi),'+str(down)+',2(up for 3chi),'+str(up)+',0(nu),'+str(nu)+',Total,'+str(jj)+',Date,'+tdate+',File,'+ffname+'\n'
      f.write(cont)
      cont=str(maxval)+','+maxtag+','+str(jj)+','+tdate+','+str(maxval/jj)+','+ffname+'\n'
      f.write(cont)
      ins_listofnews(tdate,str(jj),str(down),str(up),str(nu),str(maxval),maxtag,ffname)


        

     
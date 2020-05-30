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

def sel_listofnews(filenm,ddate):
  dbname='news'
  #use news for news server
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y%m%d")
  if (ddate==''):
    ddate=tdate
  print ("sel date",ddate)
  
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    
    sql1="select * from listofnews  where "
    sql2="tdate="+"'"+ddate+"'"+ " and filenm like "+"'%"+filenm+"%'"
    

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
#********************************
#main**************
args = sys.argv
target=args[1]
ff=open(target,'r')
news=ff.readline()
print (news)
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

nextd=now + timedelta(days=1)
ndate=nextd.strftime("%Y%m%d")
if (args[3]=='t'):
  ndate=todaydate
writefile=args[2]+ndate+'.csv'
print (writefile)
with open(writefile, 'w') as f:
  if (1):
    


    maxval=0
    maxtag='-'
    msg=''
    jj=0
    modelno=0
    msgtop='このメールは、センチメント分析の結果で3日後の日経VIの変動を予測するものです。\n'+'モデルによって結果が異なります。\n'
    f.write(msgtop)
    for nn in nw:
      #print (nn)    
      data=[]
      maxval=0
      
      if (nn==''):
        print ("No more")
        continue
      
      res=sel_listofnews(nn,ndate)
      
      

      for rr in res:
        modelno=modelno+1
       

        print (modelno) 
        down=rr[3]
        up=rr[4]
        nu=rr[5]
        total=rr[2]
        maxval=rr[6]
        maxtag=rr[7]
        filenm=rr[8]

        msgmodel="MODEL NO:"+str(modelno)+">>"
        msg0=str(ndate)
        msg1='今日 '+msg0+' の分析結果は、以下のとおりです。'
        if (maxtag=='0'):
          msg2='日経VIは変動なし。'
        elif (maxtag=='1'):
          msg2='日経VIは下がります。'
        else:
          msg2='日経VIは上がります。'
        msg3='その確率は、'+str(maxval/total)[0:5]+'です。'
        print (msgmodel+msg1+msg2+'\n'+msg3)
        f.write(msgmodel+msg1+msg2+'\n'+msg3+'\n')
        #print ("maxtag:",maxtag)
        #print ("%",str(maxval/total)[0:5])
        msg11='それぞれの確率は、'
        msg12='下がるが、'+str(down/total)[0:5]+'です。'
        msg13='上がるが、'+str(up/total)[0:5]+'です。'
        msg14='変動なしが、'+str(nu/total)[0:5]+'です。'
        print (msg11+msg12+msg13+msg14)
        #cont='1(down),'+str(down)+',2(up),'+str(up)+',0(nu),'+str(nu)+',Date,'+tdate+',File,'+nn+'\n'
        #print (cont)
        f.write(msg11+msg12+msg13+msg14+"DL:"+filenm[9:19]+'\n')
        #cont=str(maxval)+','+maxtag+','+str(total)+','+tdate+','+str(maxval/total)+','+nn+'\n'
      #f.write(cont)
        #print (cont)


        

     
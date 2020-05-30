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
import scrape_d
import scrape_b
#import sentimentj
def check (i):
  if ('\u3040'<=i<='\u309F' or '\u30A0'<=i<='\u30FF' or '\u0030'<=i<='\u0039' or '\u0041'<=i<='\u005A' or '\u0061'<=i<='\u007A' or '\u3000'<=i<='\u303F' or  '\u4e00'<=i<='\u9fff' or '\uFF00'<=i<='\uFFEF' or '\u0000'<=i<='\u007F'):
    return True

  return False

def find_junk(text):
  junk=['スポーツ']
  if (text in junk):
    return True
  else:
    return False

def sel_rss(pt):
  
  #dbname=drive_config.read_config('/tmp/configfile')
  dbname='medex13a'
  items=[]
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  #encode='utf-8'
  #cur.execute("set client_encoding to '%s'" % encode)
  try:
    rows=[]
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select "a0" from nsnote where "Superseded" is null and "患者"='+ str(pt)+'  order by "ObjectID" desc limit 1000'
    print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    if (len(rows)):
      for rr in rows:
        items.append(rr[0])
      return items
    else:
      return False
    
    
  except (Exception, psycopg2.DatabaseError) as error:
    items=[]
  finally:
    if conn is not None:
      conn.close()
def sel_pt(ptno):
  dbname='medex13a'
  items=[]
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    rows=[]
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select ptid from tbl_pt where pt_no='+"'"+ptno+"'"
    print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    return rows[0][0]
  except (Exception, psycopg2.DatabaseError) as error:
    pass
  finally:
    if conn is not None:
      conn.close()
#added type to nsnotte  
def find_a(pt,a):
  dbname='medex13a'
  items=[]
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    rows=[]
    ab='%'+a+'%'
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select "ID" from nsnote where "患者"='+"'"+pt+"'"+' and a0 like '+"'"+ab+"'"
    #print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    return len(rows)
  except (Exception, psycopg2.DatabaseError) as error:
    pass
  finally:
    if conn is not None:
      conn.close()

def ins_nsnote_rss2(pt,aa,bb,cc,dd,ee):
  dbname='medex13a'
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  #print ("INS")
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  #bb = unicode(bb, errors='ignore')
  #encode='utf-8'
  #cur.execute("set client_encoding to '%s'" % encode)
  try:
    sql = """INSERT INTO nsnote("患者", a0,a1,recordon,"OrderDate","tag","sc","tag2") 
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s) """
    cur.execute(sql, (pt,aa,bb,now,tdate,cc,dd,ee))
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    print ("ERROR INS")
    pass
  finally:
    if conn is not None:
      conn.close()
  return 
def ins_nsnote_rss(pt,aa,bb):
  dbname='medex13a'
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  #tdate=now.strftime("%Y-%m-%d")  
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  #bb = unicode(bb, errors='ignore')
  encode='utf-8'
  cur.execute("set client_encoding to '%s'" % encode)
  try:
    sql = """INSERT INTO nsnote("患者", a0,a1,recordon,"OrderDate") 
    VALUES(%s,%s,%s,%s,%s) """
    cur.execute(sql, (pt,aa,bb,now,tdate))
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    pass
  finally:
    if conn is not None:
      conn.close()
  return 
def read_sent(file):
  sents=[]
  with open(file) as fp:
    s = fp.read()
    sents=s.split('\n')
    
  return sents
def find_num(moji):
  nums=['0','1','2','3','4','5','6','7','8','9','.','-']
  wk=''
  for m in moji:
    if m in nums:
      wk=wk+m
    else:
      break
    
  return wk
#pt=251935 -010 252031 -110
def scrrss(ptno,url,wtype,main):
  import sentimentj
    
    if (main==''):
        main='00000200'
    

    mainid=sel_pt(main)
    print (mainid)
    
    pt=sel_pt(ptno)
    #pt=sel_pt('00000200')
    print (pt)
    items=sel_rss(pt)

    
    #print (items)
    #pt=251935
    #ff=open('/tmp/sentiment.txt','w')
#page = requests.get("https://assets.wor.jp/rss/rdf/nikkei/news.rdf")
    page=requests.get (url)
#"https://assets.wor.jp/rss/rdf/reuters/top.rdf"
#page=requests.get("https://feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Fassets.wor.jp%2Frss%2Frdf%2Fnikkei%2Fnews.rdf")
#page
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#rr=soup.find_all('a')
    rr=soup.select("title")
    print ("Count:",len(rr))
    i=0
    news=[]
    for r in range(len(rr)):
        wline=rr[r]
    
        i+=1
    
        ww=wline.get_text()
        news.append(str(i)+":"+ww[:])

    rr=soup.find_all("item")
    i=0
    link=[]
    cont=[]
    for r in range(len(rr)):
        wline=rr[r]
    
        i+=1
        bb=wline.title.text
        
        subb=bb[:]

        #print (bb)
        exist=False
        #2020-03-03
        '''
        subu=subb.encode("utf-8")
        print (subu)
        if (len(items)>0):
          for k in items:
              #wtt=tt.decode("utf-8")
            
              if (k.find(subu)):
                  print ("exist")
                  exist=True
                  break
              else:
                  exist=False  
    
          if (exist):
              continue
    
          '''
            
        

    #bb=wline.text
        wbb=bb.replace("\\n"," ")
        aa=wline.attrs['rdf:about']
        waa=aa.replace("\\n"," ")
        ff=find_a(pt,waa)
        if (ff):
          print ('exist')
          continue
    

        if (wtype=='b'):
          detail=scrape_b.scrape_b(waa,wtype)
          wdsub=detail
        else:
          detail=scrape_d.scrape_d(waa,wtype)


        
          wd=detail.encode('utf-8')
        #wd=wd+'.'
          wd=wd.replace('"','')
          wd=wd.replace(",",'、')
          wd=wd.replace("【",'')
        #】
          wd=wd.replace("】",'、')
        
          ff=wd.find('datePublished')
          if (ff):
            wdsub=wd[0:ff]
          
          else:
            wdsub=wd[:]
        
        

        

        if (wtype=='b'):
          color="#000000"
          sc=''
          wtotal=''
          print ("Bloom:"+wdsub)


        else:        
          sentimentj.analyzetxt(wdsub)
          ss=read_sent('/tmp/score_only')
        
          sc=''
          for s in ss:
          #if (s.find('total')>=0):
           #   totalsc=s
            sc=sc+s+"<br>"
            
          print (sc)
          ts=sc.find('total')
        #show only 4 digits
          wk=sc[ts+6:ts+10]
          wtotal=find_num(wk)
          print (wtotal)
          ff=0
          if (wtotal[0]=='-'):
            ff=1
          else: 
            wtotal='+'+wtotal
        
          ff=sc.find('-')
          print ("find -",ff)
          if (ff>0):
            color="red"
          else:
            color="#000000"
        
        #color="#000000"
        #sc=''
        #wtotal=''
        if (wtype=='b'):
          xx='Bloom'
        else:
          xx='ABC'
        abc='<div>'+'<a href="'+waa+'" target="_blank" style="color:'+color+'">'+xx+'</font></a>'
        print (abc)
        wabc=abc.encode('utf-8')

        ins_nsnote_rss2(pt,wabc,wdsub,sc,wtotal,wtype)

        ins_nsnote_rss2(mainid,wabc,wdsub,sc,wtotal,wtype)

#allscrape3.py 
def scrrss3(ptno,url,wtype,main):

    
    if (main==''):
        main='00000200'
    

    mainid=sel_pt(main)
    print (mainid)
    
    pt=sel_pt(ptno)
    #pt=sel_pt('00000200')
    print (pt)
    items=sel_rss(pt)

    
    #print (items)
    #pt=251935
    #ff=open('/tmp/sentiment.txt','w')
#page = requests.get("https://assets.wor.jp/rss/rdf/nikkei/news.rdf")
    page=requests.get (url)
#"https://assets.wor.jp/rss/rdf/reuters/top.rdf"
#page=requests.get("https://feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Fassets.wor.jp%2Frss%2Frdf%2Fnikkei%2Fnews.rdf")
#page
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#rr=soup.find_all('a')
    rr=soup.select("title")
    print ("Count:",len(rr))
    i=0
    news=[]
    for r in range(len(rr)):
        wline=rr[r]
    
        i+=1
    
        ww=wline.get_text()
        news.append(str(i)+":"+ww[:])

    rr=soup.find_all("item")
    i=0
    link=[]
    cont=[]
    for r in range(len(rr)):
        wline=rr[r]
    
        i+=1
        bb=wline.title.text
        
        subb=bb[:]

        #print (bb)
        exist=False
        
        wbb=bb.replace("\\n"," ")
        aa=wline.attrs['rdf:about']
        waa=aa.replace("\\n"," ")
        ff=find_a(pt,waa)
        if (ff):
          print ('exist')
          continue
    

        if (wtype=='b'):
          detail=scrape_b.scrape_b(waa,wtype)
          wdsub=detail
        else:
          detail=scrape_d.scrape_d(waa,wtype)


        
          wd=detail.encode('utf-8')
        #wd=wd+'.'
          wd=wd.replace('"','')
          wd=wd.replace(",",'、')
          wd=wd.replace("【",'')
        #】
          wd=wd.replace("】",'、')
        
          ff=wd.find('datePublished')
          if (ff):
            wdsub=wd[0:ff]
          
          else:
            wdsub=wd[:]
        
        

        

        if (wtype=='b'):
          color="#000000"
          sc=''
          wtotal=''
          print ("Bloom:"+wdsub)


        else:        
          
          color="#000000"
        
        
          sc=''
          wtotal=''
        if (wtype=='b'):
          xx='Bloom'
        else:
          xx='ABC'
        abc='<div>'+'<a href="'+waa+'" target="_blank" style="color:'+color+'">'+xx+'</font></a>'
        print (abc)
        wabc=abc.encode('utf-8')

        ins_nsnote_rss2(pt,wabc,wdsub,sc,wtotal,wtype)

        ins_nsnote_rss2(mainid,wabc,wdsub,sc,wtotal,wtype)


if __name__=='__main__':
  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument(
      'pt',
      help='pt')
  parser.add_argument(
      'url',
      help='url')
  parser.add_argument(
      'type',
      help='type')
  parser.add_argument(
      'main',
      help='main')
    
  args = parser.parse_args()
    
  scrrss(args.pt,args.url,args.type,args.main)

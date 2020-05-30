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
import unicodedata
#import emoji
import re
import string

all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)
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
    #print (sql)    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    #sql ='select "ID" from nsnote where a0 like '+"'"+ab+"'"
    #print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    return len(rows)
  except (Exception, psycopg2.DatabaseError) as error:
    pass
  finally:
    if conn is not None:
      conn.close()

# Turn a Unicode string to plain ASCII, thanks to https://stackoverflow.com/a/518232/2809427
def unicode2ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )


def unicodetoascii(text):

    aaa = (text.
            replace('\xe2\x80\x99', "'").
            replace('\xc3\xa9', 'e').
            replace('\xe2\x80\x90', '').
            replace('\xe2\x80\x91', '').
            replace('\xe2\x80\x92', '').
            replace('\xe2\x80\x93', '').
            replace('\xe2\x80\x94', '').
            replace('\xe2\x80\x94', '').
            replace('\xe2\x80\x98', "").
            replace('\xe2\x80\x9b', "").
            replace('\xe2\x80\x9c', '').
            replace('\xe2\x80\x9c', '').
            replace('\xe2\x80\x9d', '').
            replace('\xe2\x80\x9e', '').
            replace('\xe2\x80\x9f', '').
            replace('\xe2\x80\xa6', '').#
            replace('\xe2\x80\xb2', "").
            replace('\xe2\x80\xb3', "").
            replace('\xe2\x80\xb4', "").
            replace('\xe2\x80\xb5', "").
            replace('\xe2\x80\xb6', "").
            replace('\xe2\x80\xb7', "").
            replace('\xe2\x81\xba', "").
            replace('\xe2\x81\xbb', "").
            replace('\xe2\x81\xbc', "").
            replace('\xe2\x81\xbd', "").
            replace('\xe2\x81\xbe', "")

                 )
    return aaa

def sel_rss(pt,tbl):
  
  #dbname=drive_config.read_config('/tmp/configfile')
  dbname='medex13a'
  items=[]
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  #12-12-2019
  encode='utf-8'
  cur.execute("set client_encoding to '%s'" % encode)
  try:
    rows=[]
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select "a0" from '+tbl+' where "Superseded" is null  and "患者"='+ str(pt)+'  order by "ObjectID" desc limit 1000'
    #print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    for rr in rows:
        items.append(rr[0])
    return items
    
    
  except (Exception, psycopg2.DatabaseError) as error:
    pass
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
  
def ins_nsnote_rss(pt,tbl,aa,bb,cc,dd):
  dbname='medex13a'
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  #tdate=now.strftime("%Y-%m-%d")  
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  #12-12-2019
  bb = unicode(bb, errors='ignore')
  #encode='utf-8'
  #cur.execute("set client_encoding to '%s'" % encode)
  try:
    head='insert into '+tbl
    sql = """ ("患者", a0,a1,recordon,"OrderDate","tag","sc") 
    VALUES(%s,%s,%s,%s,%s,%s,%s) """
    sqla=head+sql
    cur.execute(sqla, (pt,aa,bb,now,tdate,cc,dd))
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


    #use this 

def scrrss2(ptno,tbl,url,wtype):
    #for yahoo news
    pt=sel_pt(ptno)
    #ptmain=sel_pt('00000200')
    items=sel_rss(pt,tbl)
    
    page=requests.get (url)

#page=requests.get ("https://news.yahoo.com/politics/")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    rr=soup.select("a")
    i=0

    for r in range(len(rr)):
        wline=rr[r]
        abc=wline.text
        i+=1
        if (i>300):
            break
        if ('href' in wline.attrs):
            #url link
            waa=wline.attrs['href']
            if (find_a(pt,waa)):
              print ("Exist")
              continue
            
            waaurl=url+waa
            #print (waaurl)
        #if ("headline" in waa):
            page2=requests.get (waaurl)
            soup2 = BeautifulSoup(page2.content, 'html.parser')

            xx=soup2.select('p')
            j=0
            bb=''
            for x in xx:
                j+=1
                if (j>100):
                    break
                bb=bb+' '+x.get_text()
            #print (bb)
            esw=0
            
            uabc=abc.encode('utf-8')
            mabc=uabc.replace("'","")
            
            #detail 
            ubb=bb.encode('utf-8')
            ubb=ubb.replace("'","")
            
            ubb=ubb.replace("\\n","")
            ubb=ubb.replace("\\r","")
            ubb=ubb.replace("\\t","")
            
            
        
            wd=ubb.replace('"','')
            wd=wd.replace(",",'、')
            wd=wd.replace("【",'')
        
            wd=wd.replace("】",'')
        
        
            ff=wd.find('datePublished')
            if (ff):
              wdsub=wd[0:ff]
              #print (wdsub)
            else:
              wdsub=wd

            if (len(wdsub)>1000):
              wds=wdsub[0:1000]
            else:
              wds=wdsub[:]
            
            if (len(wds)==0):
              continue
            print (wds)
            ff=0
            wtotal=''
            sc=''

            '''
            sentimentj.analyzetxt(ubb)            
            ss=read_sent('/tmp/score_only')
            #wd=detail.encode('utf-8')
            #url link
            #uwaa=waaurl.encode('utf-8')
            
            sc=''
            wtotal=''
            
            for s in ss:
                sc=sc+s+"<br>"
            #print (sc)
            ts=sc.find('total')
            wk=sc[ts+6:]
            wtotal=find_num(wk)
            #print (wtotal)
            ff=0
            if (wtotal[0]=='-'):
                ff=1
            else: 
                wtotal='+'+wtotal                        
            #ff=sc.find('-')
            '''

            if (ff>0):
                color="red"
            else:
                color="#000000"
            

            
            
            uurl=waaurl.encode('utf-8')
            
            
            wurl='<div>'+'<a href="'+uurl+'" target="_blank" style="color:'+color+'">YAHOOUS'+'</a>'
            #print ("CONT:",ubb)
            
            

            #wurl='<div>'+'<a href="'+uwaa+'" target="_blank" ><font color="#000000" >'+wd+'</font></a>'
            #print ("URL:",wurl)
            #11-18-2019
            ins_nsnote_rss(pt,tbl,wurl,wds,sc,wtotal)
            #ins_nsnote_rss(ptmain,wurl,ubb,sc,wtotal)
            
           
            
        
        

    
    
    


if __name__=='__main__':
  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument(
      'ptno',
      help='ptno')
  parser.add_argument(
      'tbl',
      help='tbl')
  parser.add_argument(
      'url',
      help='url')
  parser.add_argument(
      'type',
      help='type')
    
  args = parser.parse_args()
    
  scrrss2(args.ptno,args.tbl,args.url,args.type)

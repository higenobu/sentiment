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


def c2f(ptno,seldate,tbl):
  if (ptno=='0'):
    ww=' from '+tbl+ ' where '
  else:
    pt=sel_pt(ptno)
    ww=' from '+tbl+ ' where "患者"='+str(pt)+' and '
  
  sql='''copy  (select "OrderDate",
  "患者",
  a0,
  recordon,  
  a1,  
  b1,  
  b2 ,
  taglist,
  tag,
  tag2,
  sc '''
  sqla=sql+ww+' recordon >='+"'"+str(seldate)+"'"+"  ) to '/tmp/scr200'"+" delimiter ';'"

  dbname='medex13a'
  
  
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    
    print (sqla)
    cur.execute(sqla)
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    pass
  finally:
    if conn is not None:
      conn.close()
  return 


def f2c(tbl):
  sqle='copy  '+ tbl+'("OrderDate","患者",a0,recordon,  a1,  b1,  b2 ,taglist,tag,tag2,sc) from'+" '/tmp/scr200' delimiter ';'"
  

  
  dbname='medex13a'
  
  
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    
    print (sqle)
    cur.execute(sqle)
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    pass
  finally:
    if conn is not None:
      conn.close()
  return 





def copynews(ptno,seldate,tbl,newtbl):
  c2f(ptno,seldate,tbl)
  f2c(newtbl)
  return

def sel_news(pt,select_date,table_name):
  
  #dbname=drive_config.read_config('/tmp/configfile')
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  ydate=yes.strftime("%Y-%m-%d")
  dbname='medex13a'
  items=[]
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    rows=[]
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select "a0","a1","OrderDate","recordon" from  '+table_name+' where "患者"='+ str(pt)+' and "recordon">='+"'" + select_date+"'"+'   order by "ObjectID" desc '
    #print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    '''
    for rr in rows:
        items.append(rr[0])
    '''
    return rows
    
    
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

def ins_news(newsid,newsdate,s2,t2,t1):
  dbname='news'
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  table_name='news'
  
  s2=s2.replace("'","")
  t2=t2.replace("'","")
  t1=t1.replace("'","")
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    sql = 'INSERT INTO "'+table_name+'"'+ ' (newsid,newsdate,s2,t2,t1) '+ 'values('+"'"+newsid+"',"+"'"+newsdate+"',"+"'"+s2+"',"+"'"+t2+"',"+"'"+t1+"')"
    cur.execute(sql)
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
  nums=['1','2','3','4','5','6','7','8','9','0']
  #zen=['１','２','３','４','５','６','７','８','９','０']
  wk=''
  for m in moji:
    if m in nums:
      wk=wk+m
    else:
      break
    
  return wk
def conv_num(cont):
  han={u'１':u'1',u'２':u'2',u'３':'3',u'４':'4',u'５':'5',u'６':'6',u'７':'7',u'８':'8',u'９':'9',u'０':'0'}
  #zen=['１','２','３','４','５','６','７','８','９','０']
  #han='1234567890'
  #zen='１２３４５６７８９０'
  ans=''
  contu=cont.encode('utf-8')
  for z in cont:
    ans=ans+han[z]

  
  return ans
  

def read_news(seldate,fname):
    #print (seldate)
    #print (fname)
    #han={u'１':u'1',u'２':u'2'}
  
    #
    
    #for z in zz:
    #  print (han[z])
  
  

    #pt2=sel_pt(newptno)
    #pt=sel_pt(ptno)
    #rr=sel_news(seldate,fromtbl)
    #print ("number of news:",len(rr))
    #past_news=sel_news(pt2,seldate,tblname)
    
    nfile=open(fname,'r')
    data=nfile.readline()
    k=0
    dt4=''
    newsid='0'
    newsdate='2019-01-01'
    s2=''
    s1=''
    t1=''

    while (data and k<1000000000):
      ff=0
      #print (data)
      #◇
      data=data.replace("▲","")
      data=data.replace("◇","")
      ff=data.find("＼ＩＤ＼")      
      if (ff>=0):
        print (50*'*')
        #print ("04;"+dt4)
        t2=dt4
        ins_news(newsid,newsdate,s2,t2,t1)
        dt4=''
        dt=data.replace("＼ＩＤ＼","")
        dt=dt.strip('\n')
        #print ("Begining",ff)
        #print ("90;"+dt)
        k+=1

        print(conv_num(dt))
        newsid=conv_num(dt)
        
      ff=data.find("＼Ｃ０＼")      
      if (ff>=0):
        #print ("Find",ff)
        dt=data.replace("＼Ｃ０＼","")
        dt=dt.strip('\n')
        #print ("Date",ff)
        ko=conv_num(dt)
        edate= '20'+ko[0:2]+'-'+ko[2:4]+'-'+ko[4:6]      
        #print ("91;"+edate)
        newsdate=edate
      ff=data.find("＼ＡＦ＼")      
      if (ff>=0):
        #print ("Find",ff)
        dt=data.replace("＼ＡＦ＼","")
        dt=dt.strip('\n')
        #print ("92;"+dt)                
      ff=data.find("＼Ｔ１＼")      
      if (ff>=0):
        #print ("Find",ff)
        dt=data.replace("＼Ｔ１＼","")
        dt=dt.strip('\n')
        #print ("03;"+dt)
        t1=dt
      ff=data.find("＼Ｓ１＼")      
      if (ff>=0):
        #print ("Find",ff)
        dt=data.replace("＼Ｓ１＼","")
        dt=dt.strip('\n')
        #print ("01;"+dt)
        s1=dt
      ff=data.find("＼Ｓ２＼")      
      if (ff>=0):
        #print ("Find",ff)
        dt=data.replace("＼Ｓ２＼","")
        dt=dt.strip('\n')
        #print ("02;"+dt)
        s2=dt
      ff=data.find("＼Ｔ２＼")      
      if (ff>=0):
        #print ("Find",ff)
        dt=data.replace("＼Ｔ２＼","")
        dt=dt.strip('\n')
        dt4=dt4+dt
      #print ("04;"+dt4)
      

      
      data=nfile.readline()
      
    
    


    
    


if __name__=='__main__':
  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  
  parser.add_argument(
      'tdate',
      help='tdate')
  
  parser.add_argument(
      'fname',
      help='fname')
  '''
  parser.add_argument(
      'tname',
      help='tname')
 
  parser.add_argument(
      'tpt',
      help='tpt')
  '''  
  args = parser.parse_args()
    
  #copy2main_news(args.pt,args.tdate,args.fname,args.tname,args.tpt)
  read_news(args.tdate,args.fname)
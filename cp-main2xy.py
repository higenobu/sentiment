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
def find_junk(text):
  junk=['スポーツ']
  if (text in junk):
    return True
  else:
    return False

def c2f(ptno,seldate,tbl):
  if (ptno=='0'):
    ww=' from '+tbl+ ' where '
  else:
    pt=sel_pt(ptno)
    ww=' from '+tbl+ ' where "Superseded" is null  and 患者"='+str(pt)+' and '
  
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
  sqla=sql+ww+' recordon >='+"'"+str(seldate)+"'"+"  ) to '/tmp/scr2000'"+" delimiter ';'"

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
  sqle='copy  '+ tbl+'("OrderDate","患者",a0,recordon,  a1,  b1,  b2 ,taglist,tag,tag2,sc) from'+" '/tmp/scr2000' delimiter ';'"
  

  
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
def find_news(pt,select_date,wd,table_name):
  #check only a0 (URL)
  #dbname=drive_config.read_config('/tmp/configfile')
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  ydate=yes.strftime("%Y-%m-%d")
  dbname='medex13a'
  word='%'+wd+'%'
  items=[]
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  #encode='utf-8'
  #cur.execute("set client_encoding to '%s'" % encode)
  try:
    rows=[]
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select "ObjectID" from  '+table_name+' where "Superseded" is null and  "患者"='+ str(pt)+' and "OrderDate">='+"'" + select_date+"'"+' and a0  like '+"'"+word+"'"
    #print (sql)
    cur.execute(sql)

    rows = cur.fetchall()
    
    return len(rows)
    
    
  except (Exception, psycopg2.DatabaseError) as error:
    pass
  finally:
    if conn is not None:
      conn.close()

def sel_news(pt,select_date,table_name):
  
  #dbname=drive_config.read_config('/tmp/configfile')
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  ydate=yes.strftime("%Y-%m-%d")
  dbname='medex13a'
  items=[]
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  encode='utf-8'
  cur.execute("set client_encoding to '%s'" % encode)
  try:
    rows=[]
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select "a0","a1","OrderDate","recordon","b2","tag2","sc","ObjectID" from  '+table_name+' where "Superseded" is null and  "患者"='+ str(pt)+' and "OrderDate">='+"'" + select_date+"'"+' and a1 not like '+"'%スポーツ%'"+'   order by "ObjectID" desc '
    print (sql)
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

def ins_news(rr,pt,table_name):
  dbname='medex13a'
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  #print (rr)

  aa=rr[0]
  bb=rr[1]
  #2020-05-04
  bb=bb.replace("'","")
  bb=bb.replace('"',"")
  cc=str(rr[2])
  dd=str(rr[3])
  ee=rr[4]
  ff=rr[5]
  gg=rr[6]
  hh=rr[7]
  #print (ee)
  #do not insert if junk
  '''
  if (find_junk(aa)):
    print ('junk',aa)
    return
  if (find_junk(bb)):
    print ('junk',bb)
    return 
  '''

  if(ee==None):
    ee=' '
  if(ff==None):
    ff=' '
  if(gg==None):
    gg=' '
  
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  #12-12-2019
  #encode='utf-8'
  #cur.execute("set client_encoding to '%s'" % encode)
  #no recordon
  try:
    sql = 'INSERT INTO "'+table_name+'"'+ ' ("患者", a0,a1,"OrderDate","b2","tag2","sc","oid") '+ 'values('+"'"+str(pt)+"',"+"'"+aa+"',"+"'"+bb+"','"+cc+"',"+"'"+str(ee)+"',"+"'"+str(ff)+"',"+"'"+str(gg)+"','"+str(hh)+"'"+")"
    #print (sql)
    cur.execute(sql)
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    pass
  finally:
    if conn is not None:
      conn.close()
  return 
def del_news(ptno,select_date,table_name):
  dbname='medex13a'
  now=datetime.datetime.now()
  yes=now + timedelta(days=-1)
  tdate=now.strftime("%Y-%m-%d")
  pt=sel_pt(ptno)
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    sql = 'delete from  "'+table_name+'"'+ ' where "患者"='+"'"+str(pt)+"'"+' and "OrderDate" < '+"'"+select_date+"'"
    print (sql)
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
  nums=['0','1','2','3','4','5','6','7','8','9','.','-']
  wk=''
  for m in moji:
    if m in nums:
      wk=wk+m
    else:
      break
    
  return wk
def exist(ss,slist):
  find=0
  #ss=ss.replace('"',"")
  #ss=ss.replace("'","")
  for m in slist:
    
    
    if (ss==m):
      print ("EXIST")
      find=1
      break

    else:
      continue
    
  if (find==0):
    return False
  else:
    return True


#check duplicate and use this module fro copy from nsnote to nsnotex2 , nsnotex4
def cnews(ptno,seldate,fromtbl,tblname):
    print (seldate)
    print (fromtbl)
    print (tblname)
    #pt2=sel_pt(newptno)
    pt=sel_pt(ptno)
    print (pt)
    now=datetime.datetime.now()
    yes=now + timedelta(days=-1)
    tdate=now.strftime("%Y-%m-%d")
    print (tdate)
    seldate=tdate
    main=0
    #if ptno is not 200 then insert to 200 also
    if (ptno=='00000200'):
      pass
    else:
      ptmain='00000200'
      main=sel_pt(ptmain)

    
    rr=sel_news(pt,seldate,fromtbl)
    print ("number of news:",len(rr))
    '''
    past_news=sel_news(pt,seldate,tblname)
    aa=[]
    i=0
    wlist=[]
    for i in range(len(past_news)):
      pp=past_news[i][0]
      #pp=pp.replace('"',"")
      #pp=pp.replace('target=_blank style=color:red>',"")
      #print (pp)
      aa.append(pp)
    #print (aa)
    '''
#find_news(pt,select_date,wd,table_name):
    for k in range(len(rr)):
      aa=find_news(pt,seldate,rr[k][0],tblname)
      if (aa):
        print ('exist:'+rr[k][0])
        continue
      else:
        ins_news(rr[k],pt,tblname)
      if (main>0):
        bb=find_news(main,seldate,rr[k][0],tblname)
        if (bb):
        #print ('exist:'+rr[k][0])
          continue
        else:
          ins_news(rr[k],main,tblname)

    




    
    


if __name__=='__main__':
  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument(
      'pt',
      help='pt')
  
  parser.add_argument(
      'tdate',
      help='tdate')
  
  parser.add_argument(
      'fname',
      help='fname')
  parser.add_argument(
      'tname',
      help='tname')
  args = parser.parse_args()
  

  cnews(args.pt,args.tdate,args.fname,args.tname)
  #copynews(args.pt,args.tdate,args.fname,args.tname)
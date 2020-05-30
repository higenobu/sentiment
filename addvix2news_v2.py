#!/usr/bin/env python
import sys
import csv
#import mojimoji
import time
import datetime
from datetime import timedelta
import random
def find_date(sub,data):
    '''
    wdate=sub.split('-')
    wy=int(wdate[0])
    wm=int(wdate[1])
    wd=int(wdate[2])
    x=datetime.datetime(wy,wm,wd)
    dx=x.strftime("%Y-%m-%d")
    dd1=x+timedelta(days=1)
    dd2=x+timedelta(days=1)
    dd3=x+timedelta(days=1)
    d1=dd1.strftime("%Y-%m-%d")
    d2=dd2.strftime("%Y-%m-%d")
    d3=dd3.strftime("%Y-%m-%d")
    '''

    for i in range(len(data)):
        
        #print (j)
        if (sub==data[i]):
            print ("find"+sub+"***"+str(i))
            break
    else:
        return int(-1)

    return i
        




args = sys.argv
#nikkei-vix-data
#tagpos=int(args[4])

with open(args[1]) as h:
    reader = csv.reader(h, delimiter=';')
    lg = [row for row in reader]
    
    vixdata=[]
    vixdt=[]
    ii=0
    for m in lg:
        #print (m[0])
        vixdata.append(m[1])
        vixdt.append(m[0])
        
        ii+=1
    print ("vix:",ii)


with open(args[2]) as f:
    reader = csv.reader(f, delimiter=';')
    ls = [row for row in reader]

    result_ls = []
    dup=[]
    tag=[]
    k=0
    j=0
    for l in ls:

        #print (len(l))
        if (len(l)==0):
            continue
        if (len(l[1])<50):
            print ("skip")
            print (l[1])
            continue
        #print (l[0])
        #print (l[1])
        k+=1
        #date
        dd=l[0]
        print (dd)

        aa=find_date(dd,vixdt)
        print (aa)
        
        #if (sub in news):

        if (aa):
            wl=l[1]
            j+=1
            nn=wl.find("datePublished:")
            
            if (nn):
                wkk=wl[0:nn]
            else:
                wkk=wl[:]
            result_ls.append(wkk)
            tag.append(str(float(vixdata[aa])))
        else:
            print ("NO date :",l[0])

    print ("NO of records :",k)
    
    
    result_rows=[]
    print ("Output records should added :",len(result_ls))
    for k in range(len(result_ls)):
        
        result_rows.append([ result_ls[k], tag[k] ])

with open(args[3], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)



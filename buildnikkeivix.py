#!/usr/bin/env python
import sys
import csv
#import mojimoji
import time
import datetime
from datetime import timedelta
import random
#create table nikkeivix(ndate date, v1 float,v2 float,v3 float, v4 float ,v5 float,v6 float)
#copy nikkeivix from '/home/medex/nlpnews/ww-nikkeivix-0413.csv' delimiter ';';
#up to 2020-04-13
def find_date(sub,data):
    
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
    reader = csv.reader(h, delimiter=',')
    lg = [row for row in reader]
    
    vixdata=[]
    vixdt=[]
    ii=0
    for m in lg:
        #print (m[0])
        
        vixdt.append(m[0])
        vixdata.append([m[1],m[2],m[3],m[4],m[5],m[6]])
        
        ii+=1
    print ("vix:",ii)

rdate=[]
rdata=[]
x=datetime.datetime(2017,1,1)
pastdata=[]
for i in range(3000):
        
        
        dd=x+timedelta(days=i)
        dx=dd.strftime("%Y-%m-%d")
        if (dx>'2020-04-13'):
            break

        print (dx)
        aa=find_date(dx,vixdt)
        if (aa>=0):
            rdate.append(dx)
            rdata.append(vixdata[aa])
            print (vixdata[aa])
            pastdata=vixdata[aa]
        else:
            rdate.append(dx)
            print ("add pastdata")
            print (pastdata)
            rdata.append(pastdata)            



    
    
result_rows=[]
print ("Output records should added :",len(rdata))
for k in range(len(rdata)):
    if (len(rdata[k])>0):
        print (rdate[k]) 
        print (rdata[k])  
        result_rows.append([ rdate[k], rdata[k][0],rdata[k][1],rdata[k][2],rdata[k][3],rdata[k][4],rdata[k][5]])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(result_rows)



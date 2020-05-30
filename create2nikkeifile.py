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
#select ndate,v5 from nikkeivix where v5>1.0 or v5<-1.0 order by ndate asc;
#copy(select ndate,v5 from nikkeivix where v5>1.0 or v5<-1.0 order by ndate asc) to '/tmp/nikkeivix-v3.csv' delimiter ';'
def find_date(sub,data):
    
    for i in range(len(data)):
        
        #print (j)
        if (sub==data[i]):
            #print ("find"+sub+"***"+str(i))
            break
    else:
        return int(-1)

    return i
        




args = sys.argv
#nikkei-vix-data
startdate=args[3]
enddate=args[4]
tag=args[5]
print (startdate)
print (enddate)
#nikkei-vix-original
with open(args[1]) as h:
    reader = csv.reader(h, delimiter=',')
    lg = [row for row in reader]
    
    vixdata=[]
    vixdt=[]
    ii=0
    for m in lg:
        #print (m[0])
        
        vixdt.append(m[0])
        vixdata.append([m[1],m[2],m[3],m[4],m[5]])
        
        ii+=1
    print ("no of vix:",ii)

rdate=[]
rdata=[]
#2020-01-01
sy=startdate[0:2]
sm=startdate[3:5]
sd=startdate[6:8]
print (sy+sm+sd)
sy='20'+sy

x=datetime.datetime(int(sy),int(sm),int(sd))
pastdata=[]
for i in range(3000):
        
        
        dd=x+timedelta(days=i)
        dx=dd.strftime("%Y-%m-%d")
        if (dx>enddate):
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
        result_rows.append([ rdate[k], rdata[k][int(tag)]])
#nikkei-vix: (date,value)
with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(result_rows)



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
            #print ("find"+sub+"***"+str(i))
            break
    else:
        return int(-1)

    return i
        
    


args = sys.argv
#collect vi data
future=args[3]
print ("advanced date",future)
with open(args[1]) as h:
    reader = csv.reader(h, delimiter=',')
    lg = [row for row in reader]
    
    vixdata=[]
    vixdt=[]
    ii=0
    for m in lg:
        #print (m[0])
        
        vixdt.append(m[0])
        vixdata.append([m[1],m[2],m[3],m[4]])
        
        ii+=1
    print ("vix:",ii)
    

rdate=[]
outdate=[]
outval=[]
rval=[]
jdate=[]
jval=[]
x=datetime.datetime(2020,05,15)
pastval=0
for i in range(3000):
        
        
        dd=x+timedelta(days=-i)
        dx=dd.strftime("%Y-%m-%d")

        if (dx<'2019-01-01'):
            break

        

        aa=find_date(dx,vixdt)
        if (aa>=0):
            val1=vixdata[aa][0]
            rval.append(val1)
            rdate.append(dx)            
            pastval=val1
            print(dx,pastval)
        else:
            print ("no date",dx)
            rdate.append(dx)
            rval.append(pastval)
print ("no of date",len(rdate))            
for i in reversed(range(len(rdate))):
    jdate.append(rdate[i])
    jval.append(rval[i])
    

for i in range(len(jdate)-1):  
    if (jdate[i]>'2020-05-08'):
        break 
    
    rrdate=jdate[i]
    rrval=jval[i]
    nextval=jval[i+int(future)]
    #print (rrdate,nextval)
    diffval=float(nextval)-float(rrval)
                
    stdiff=str(diffval)[0:5]
    print (rrdate,stdiff)
    outdate.append(rrdate)
    outval.append(stdiff) 
 
    
result_rows=[]
print ("Output records should added :",len(outdate))
for k in range(len(outdate)):
     
    result_rows.append([ outdate[k], outval[k]])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(result_rows)



import sys
import csv
#import mojimoji
import random
from datetime import date
from datetime import datetime
from datetime import timedelta

def find_date(sub,data):

    wdate=sub.split('-')
    wy=wdate[0]
    wm=wdate[1]
    wd=wdate[2]
    sub2=wy+'-'+wm+'-'+str(int(wd)+1)
    if (sub=='2019-12-01'):
        sub2='2019-12-02'
    if (sub=='2019-11-30'):
        sub2='2019-12-02'
    if (sub=='2019-12-07'):
        sub2='2019-12-09'
    if (sub=='2020-02-01'):
        sub2='2020-02-03'
    if (sub=='2020-02-02'):
        sub2='2020-02-04'  
    if (sub=='2020-02-29'):
        sub2='2020-03-02'  
    if (sub=='2020-01-04'):
        sub2='2020-01-06'
    if (sub=='2020-01-05'):
        sub2='2020-01-07'
    if (sub=='2020-01-11'):
        sub2='2020-01-14'
    if (sub=='2019-12-31'):
        sub2='2020-01-06'
    if (sub>='2020-01-01' and sub <='2020-01-04'):
        sub2='2020-01-06'
    if (sub=='2020-03-01'):
        sub2='2020-03-03'
    if (sub=='2020-03-14'):
        sub2='2020-03-16'
    if (sub=='2020-03-07'):
        sub2='2020-03-09'                        
    sub3=wy+'-'+wm+'-'+str(int(wd)+2)
    
    for i in range(len(data)):
        if (sub==data[i] or sub2==data[i] or sub3==data[i]):
            #print (sub2)
            return i
    else:
        print ("No vix date",sub)
        return 0



args = sys.argv
#value position in nikkei-data
tagpos=int(args[2])

result_rows=[]
with open(args[1]) as h:
    reader = csv.reader(h, delimiter=',')
    lg = [row for row in reader]
    
    vixdata=[]
    vixdt=[]
    ii=0
    for m in lg:
        vixdata.append(m[tagpos])
        vixdt.append(m[0])
            
        ii+=1
    print ("vix:",ii)

    vvdate=[]
    vvcont=[]
    i=0
    for d in range(len(vixdt)):
        #print (dd)
        dd=vixdt[d]
        cont=vixdata[d]
        wdate=dd.split('-')
        wy=wdate[0]
        wm=wdate[1]
        wd=wdate[2]
        vdate=date(int(wy),int(wm),int(wd))

        #nextdate=predate+timedelta(days=1)
        if (i==0):
            print (dd+":"+cont)
            vvdate.append(dd)
            vvcont.append(cont)
            predate=vdate

            i+=1    
        if (d==(len(vixdt)-1)):
            cont='0'
            print ("last date")
            print (dd+":"+cont)
            vvdate.append(dd)
            vvcont.append(cont)
            predate=vdate

            i+=1                       
        if (vdate==predate+timedelta(days=1)):
            print (dd+":"+cont)
            vvdate.append(dd)
            vvcont.append(cont)
            i+=1
        elif (vdate==predate+timedelta(days=3)):
            ww=vdate-timedelta(days=2)
            '''
            wmm=ww.stftime("%m")
            wdd=ww.stftime("%d")
            wyy=ww.stftime("%y")
            '''
            wmm=ww.month
            wdd=ww.day
            if (wdd<10):
                strwdd="0"+str(wdd) 
            else:
                strwdd=str(wdd) 
            if (wmm<10):
                strwmm="0"+str(wmm) 
            else:
                strwmm=str(wmm)                           
            wyy=ww.year
            wwdate=str(wyy)+"-"+strwmm+"-"+strwdd
            print (wwdate+":"+cont)
            vvdate.append(wwdate)
            vvcont.append(cont)
            i+=1
            ww=vdate-timedelta(days=1)
            wmm=ww.month
            wdd=ww.day
            if (wdd<10):
                strwdd="0"+str(wdd)
            else:
                strwdd=str(wdd)
            if (wmm<10):
                strwmm="0"+str(wmm) 
            else:
                strwmm=str(wmm)                           
            wyy=ww.year
            wwdate=str(wyy)+"-"+strwmm+"-"+strwdd
            print (wwdate+":"+cont)
            vvdate.append(wwdate)
            vvcont.append(cont)
            i+=1         
            print (dd+":"+cont)   
            vvdate.append(dd)
            vvcont.append(cont)            
            i+=1

        
        predate=vdate
for k in range(len(vvdate)):
        
    result_rows.append([ vvdate[k], vvcont[k] ])

with open(args[3], 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(result_rows)

#ns-vix in ns-22
'''
with open(args[2]) as g:
    reader = csv.reader(g, delimiter=';')
    lg = [row for row in reader]
    oid=[]
    news=[]
    ii=0
    for m in lg:
        news.append(m[0])
        #tag.append(m[3])
        ii+=1
    print ("ns22-b:",ii)
#ns-vix in ns-22
'''
'''
with open(args[2]) as f:
    reader = csv.reader(f, delimiter=';')
    ls = [row for row in reader]

    result_ls = []
    dup=[]
    tag=[]
    k=0
    j=0
    for l in ls:
        k+=1
        #if l[0] in oid:
        dd=l[0]
        aa=find_date(dd,vixdt)
        
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
            tag.append(vixdata[aa])
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

'''

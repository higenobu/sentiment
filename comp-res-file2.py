
import sys
import csv
#import mojimoji
import random
from datetime import timedelta
import time
import datetime
def find_str(sub,news):

    wsub=sub[0:50]
    #wsub=wsub.replace('"','')
    for i in range(len(news)):
        wnews=news[i][0:50]
        #wnews=wnews.replace('"','')
        if (wsub==wnews):
            return i
    else:
        return 0

def find_nk(nd,values):

    #wsub=sub[0:50]
    #wsub=wsub.replace('"','')
    nd=''
    for i in range(len(values)):
        #wnews=news[i][0:50]
        #wnews=wnews.replace('"','')
        if (nd==values[i][0]):
            return values[i][1]
    else:
        return ''



args = sys.argv
#master ns-22
now=datetime.datetime.now()
#comp-res-file.py  /tmp/news-from-0404.csv /tmp/res-file.tsv 2-nikkei-vix-0421.csv   
tdate=now.strftime("%Y%m%d")
yes=now + timedelta(days=-1)
ydate=yes.strftime("%Y%m%d")
if(args[4]=='y'):
    resfile=args[2]+"_"+ydate+'.csv'
elif(args[4]=='t'):
    resfile=args[2]+"_"+tdate+'.csv'
else:
    wdate=args[4]
    resfile=args[2]+"_"+wdate+'.csv'

    print ("date"+wdate)
resfile1="comp1-"+resfile
resfile2="comp2-"+resfile
resfile='/tmp/'+resfile
ff=open("/tmp/"+resfile1,'w')
gg=open("/tmp/"+resfile2,'w')
#nikkei-vix
with open(args[3]) as nikkei:
    reader = csv.reader(nikkei, delimiter=';')
    nkl = [row for row in reader]
    
    nkdate=[]
    nkval=[]
    ii=0
    for nk in nkl:
        nkdate.append(nk[0])
        fnk=float(nk[1])
        nkval.append(fnk)
        print (fnk)
        ii+=1
    print ("nikkei:",ii)
with open(args[1]) as g:
    reader = csv.reader(g, delimiter=';')
    lg = [row for row in reader]
    oid=[]
    news=[]
    newsdate=[]
    ii=0
    for m in lg:
        newsdate.append(m[0])
        news.append(m[1])
        #print (m[1])
        ii+=1
    print ("first:",ii)
#ns-44
with open(resfile) as f:
    reader = csv.reader(f, delimiter=',')
    ls = [row for row in reader]

    result_ls = []
    dup=[]
    tag=[]
    k=0
    j=0
    s=0
    z=0
    n=0
    ndate=''
    predate=''
    for l in ls:
        k+=1
        j+=1
        #if l[0] in oid:
        if (len(l)<3):
            print ("No record")
            continue
        sub=l[4]
        #print (sub)
        sub=sub.replace(' ','')
        nscore=l[2]
        
        if(k>100000):
            break
        #aa=find_str(sub,news)
        if (k>1):
            
            ndate=newsdate[k]
            #nikkeival=find_nk(ndate,nkl)
            if (ndate==predate):
                pass
            else:
                for i in range(len(nkdate)):
        
                    if (predate==nkdate[i]):
                        nikkeival=nkval[i]
                        break
                else:
                    nikkeival=0

                ff.write(50*'-'+str(k)+"Number of 1: "+str(s)+'\n')
                print (50*'-'+str(k)+"Number of 1: "+str(s))
                wstr1=predate+',all='+str(j)+",   1="+str(s)+",   2="+str(n)+",   0="+str(z)+','
                #print ("1%="+str(float(s/j))+"   2%="+str(float(n/j))+"  0%="+str(float(z/j)))
                wstr2="score,1%="+str(float(s)/float(j))+"   , 2%="+str(float(n)/float(j))+"  , 0%="+str(float(z)/float(j))+','
                wstr3="vixval="+str(nikkeival)+','
                if (s>n):
                    if (s>z):
                        wstr4='1'
                    else:
                        wstr4='0'
                else:
                    if (n>z):
                        wstr4='2'
                    else:
                        wstr4='0'
                if (nikkeival==0):
                    val=''
                if (nikkeival<float(-1)):
                    val='1'
                elif (nikkeival>float(1)):
                    val='2'
                else:
                    val='0'
                if (val==wstr4):
                    wstr5='1'
                else:
                    wstr5='0'
                gg.write(wstr1+wstr2+wstr3+","+val+','+wstr4+','+wstr5+'\n')
                j=0
                s=0
                n=0
                z=0
            if (nscore=='1'):
                s+=1
            elif (nscore=='2'):
                n+=1
            elif (nscore=='0'):
                z+=1
            wcont=ndate+","+nscore+','+sub
            print (ndate+","+nscore+','+sub)
            ff.write(wcont+'\n')
            predate=ndate

        else:
            pass
            #print ("NO match:"+sub)
            
            
    print ("NO of records :",k)


    ff.close()
    gg.close()


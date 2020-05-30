import sys
import csv
#import mojimoji
import random
def find_date(sub,data):

    wdate=sub.split('-')
    wy=wdate[0]
    wm=wdate[1]
    wd=wdate[2]
    sub2=wy+'-'+wm+'-'+str(int(wd)+1)
    sub3=wy+'-'+wm+'-'+str(int(wd)+2)
    
    for i in range(len(data)):
        if (sub==data[i] or sub1==data[i] or sub2==data[i]):
            print (sub)
            return i
    else:
        print ("No vix date",sub)
        return 0



args = sys.argv
#master ns22-b
with open(args[1]) as h:
    reader = csv.reader(h, delimiter=';')
    lg = [row for row in reader]
    
    vixdata=[]
    vixdt=[]
    pretag=[]
    ii=0
    for m in lg:
        vixdata.append(m[4])
        pretag.append(m[2])
        
        ii+=1
    print ("result:",ii)
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
#dev.tsv data
with open(args[2]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]

    result_ls = []
    dup=[]
    tag=[]
    #trick from 1
    k=0
    j=0
    for m in range(len(ls)):
        k+=1
        if (m==0):
            m+=1
            continue
        
        
        wtag=ls[m][1]
        news=ls[m][0]
        
        
        
        #print (str(m)+vixseq[m])
        print (news+";"+vixdata[m])
        print (pretag[m]+wtag)
        if (pretag[m]=='1'):
            result_ls.append(news)
            tag.append(wtag)
        if (k>500):
            break
        

        
        

    #print ("Number  of records :",k)
    
    
    result_rows=[]
    print ("Output records should added :",len(result_ls))
    for k in range(len(result_ls)):
        
        result_rows.append([ result_ls[k], tag[k] ])

with open(args[3], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)


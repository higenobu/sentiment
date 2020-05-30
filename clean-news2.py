import sys
import csv
#import random
def check (i):

    if '\u3040'<=i<='\u309F' or '\u30A0'<=i<='\u30FF' or '\u0030'<=i<='\u0039' or '\u0041'<=i<='\u005A' or '\u0061'<=i<='\u007A' or '\u3000'<=i<='\u303F' or  '\u4e00'<=i<='\u9fff' or '\uFF00'<=i<='\uFFEF' or '\u0000'<=i<='\u007F':

        return True
    else:
        return False

#2020-05-05 check
args = sys.argv
#nikkei-vix-diff
#tagpos=int(args[4])
'''
with open(args[1]) as h:
    reader = csv.reader(h, delimiter=';')
    lg = [row for row in reader]
    
    vixdata=[]
    vixdt=[]
    ii=0
    for m in lg:
        vixdata.append(m[1])
        vixdt.append(m[0])
        
        ii+=1
    print ("vix:",ii)
'''
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
#fixed_date=args[3]
with open(args[1]) as f:
    reader = csv.reader(f, delimiter=';')
    ls = [row for row in reader]

    result_ls = []
    
    ddate=[]
    k=0
    j=0
    for l in ls:
        k+=1
        #if l[0] is OrderDate
        dd=l[0]
        #aa=find_date(dd,vixdt)
        
        #if (sub in news):
        #remove 
        if (1):
            wl=l[1]
            wl=wl.replace('"','')
            wl=wl.replace("'",'')
            wl=wl.replace(",",'')
            wl=wl.replace(".",'')
            wl=wl.replace("^",'')
            wl=wl.replace("\\r",'')
            wl=wl.replace("\\n",'')
            j+=1
            yy=wl.find("- Yahoo!ニュー")
            if (yy):
                wk1=wl[0:yy]
            else:
                wk1=wl[:]

            nn=wk1.find("datePublished:")
            
            if (nn):
                wkk=wk1[0:nn]
            else:
                wkk=wk1[:]
            validstr=''
            for wd in wkk:
                if (check(wd)):
                    validstr=validstr+wd
            print (validstr)
            result_ls.append(validstr)
            ddate.append(dd)
        

    print ("NO of records :",k)
    
    
    result_rows=[]
    print ("Output records should added :",len(result_ls))
    for k in range(len(result_ls)):
        
        result_rows.append([ddate[k],result_ls[k]])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(result_rows)



import sys
import csv
#import mojimoji
import random
def find_str(sub,news):

    wsub=sub[1:30]
    wsub=wsub.replace('"','')
    for i in range(len(news)):
        wnews=news[i][1:30]
        wnews=wnews.replace('"','')
        if (wsub==wnews):
            return i
    else:
        return 0



args = sys.argv
#master ns-22
with open(args[1]) as g:
    reader = csv.reader(g, delimiter=';')
    lg = [row for row in reader]
    oid=[]
    news=[]
    ii=0
    for m in lg:
        oid.append(m[0])
        news.append(m[1])
        ii+=1
    print ("ns22:",ii)
#ns-44
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
        sub=l[1]
        aa=find_str(sub,news)
        if (aa):
        #if (sub in news):
            print (sub)
            print (':::::::\n')
            print (news[aa])
            print ("\n")
            continue
        else:
            #check bad code?
            j+=1
            wl=l[1].replace("\n",'')
            wl=wl.replace("\r",'')
            wl=wl.replace(".",'')
            wl=wl.replace(",",'')
            nn=wl.find("datePublished:")
            wll=wl[0:nn]
            
            mm=wll.find("Yahoo!")
            wkk=wll[0:mm]
            result_ls.append(wkk)
            tag.append(l[3])
    print ("NO of records :",k)

    
    result_rows=[]
    print ("Output records should added :",len(result_ls))
    for k in range(len(result_ls)):
        
        result_rows.append([ result_ls[k], tag[k] ])

with open(args[3], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)



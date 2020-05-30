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
    reader = csv.reader(g, delimiter='\t')
    lg = [row for row in reader]
    oid=[]
    news=[]
    tag=[]
    ii=0
    for m in lg:
        tag.append(m[1])
        news.append(m[0])
        ii+=1
    print ("first file :",ii)

with open(args[2]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]

    result_ls = []
    dup=[]
    newtag=[]
    k=0
    j=0
    for l in ls:
        k+=1
        
        sub=l[0]
        aa=find_str(sub,news)
        if (aa):
        #if (sub in news):
            print (sub)
            print ('::\n')
            print (news[aa]+":"+tag[aa])
            if (tag[aa]==l[1]):
                continue
            else:
                print ("different tag")
            print ("\n")
            continue
        else:
            print ("diff:")
            j+=1
            
            result_ls.append(l[0])
            newtag.append(l[1])
    print ("NO of records :",k)

    
    result_rows=[]
    print ("Output records should added :",len(result_ls))
    for k in range(len(result_ls)):
        
        result_rows.append([ result_ls[k], newtag[k] ])

with open(args[3], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)



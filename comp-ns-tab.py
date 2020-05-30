import sys
import csv
#import mojimoji
import random
def find_str(sub,news):

    wsub=sub[0:50]
    wsub=wsub.replace('"','')
    for i in range(len(news)):
        wnews=news[i][0:50]
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
    ii=0
    for m in lg:
        #oid.append(m[0])
        news.append(m[0])
        ii+=1
    print ("first:",ii)
#ns-44
with open(args[2]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]

    result_ls = []
    dup=[]
    tag=[]
    k=0
    j=0
    for l in ls:
        
        
        sub=l[0]
        aa=find_str(sub,news)
        if (aa):
            '''
            print (sub)
            print (':::::::\n')
            print (news[aa])
            print ("\n")
            '''
            j+=1
            
        else:
            k+=1
            print ("NO match:"+sub)
            
            
    print ("same records :",j)
    print ("diff records :",k)

'''
    result_rows=[]
    print ("Output records should added :",len(result_ls))
    for k in range(len(result_ls)):
        
        result_rows.append([ result_ls[k], tag[k] ])

with open(args[3], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)
'''


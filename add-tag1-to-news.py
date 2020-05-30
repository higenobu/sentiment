import sys
import csv


args = sys.argv
#nikkei-vix-diff

#tagpos=int(args[4])
'''
with open(args[1]) as h:
    reader = csv.reader(h, delimiter=',')
    lg = [row for row in reader]
    
    vixdata=[]
    vixdt=[]
    ii=0
    for m in lg:
        vixdata.append(m[6])
        vixdt.append(m[tagpos])
        
        ii+=1
    print ("vix:",ii)

'''
#tag=1 for all news
with open(args[1]) as f:
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
        #aa=find_date(dd,vixdt)
        
        #if (sub in news):

        if (1):
            wl=l[1]
            j+=1
            nn=wl.find("datePublished:")
            
            if (nn):
                wkk=wl[0:nn]
            else:
                wkk=wl[:]
            result_ls.append(wkk)
            #tag.append(vixdata[aa])
        else:
            print ("NO date :",l[0])

    print ("NO of records :",k)
    
    
    result_rows=[]
    print ("Output records should added :",len(result_ls))
    for k in range(len(result_ls)):
        
        result_rows.append([ result_ls[k], str(1) ])

with open(args[2], 'w') as ff:
    writer = csv.writer(ff, delimiter='\t')
    writer.writerows(result_rows)



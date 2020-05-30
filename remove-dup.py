import sys
import csv
#import mojimoji
import random
args = sys.argv

with open(args[1]) as f:
    reader = csv.reader(f, delimiter=';')
    ls = [row for row in reader]

    result_ls = []
    dup=[]
    tag=[]
    k=0
    for l in ls:
        k+=1
        if l[1] in dup:
            continue
        else:
            #check bad code?
            wl=l[1].replace("\n",'')
            wl=wl.replace("\r",'')
            nn=wl.find("datePublished:")
            wll=wl[0:nn]

            dup.append(l[1])
            result_ls.append(wll)
            tag.append(l[2])
    print ("NO of records:",k)
    result_rows = []
    train=[]
    
    print ("Output records:",len(result_ls))
    for k in range(len(result_ls)):
        
        result_rows.append([ result_ls[k], tag[k] ])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)



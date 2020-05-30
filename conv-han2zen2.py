import sys
import csv
#import mojimoji
import random
args = sys.argv
#2020-03-14 updated because of null records
with open(args[1]) as f:
    ls=[]
    reader = csv.reader(f, delimiter='\t')
    # remove null recors
    for row in reader:
        if (row):
            ls.append(row)
    
    print (len(ls))
    result_ls = []
    tag=[]
    k=0
    #print (ls)
    for l in ls:
        k+=1
#        print(mojimoji.han_to_zen(l[0],ascii=False))
#        print(mojimoji.han_to_zen(l[0])
        kk=l[0]
        aa=kk.find('datePublished:')
        if (aa):
            mk=kk[0:aa]        
        else:
            mk=k[:]
        #only work python3
        zenkaku=mk.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
        print (zenkaku)
        
        
        
        #lstr=l[0].encode('utf-8')
        #result_strs = mojimoji.han_to_zen(lstr,ascii=False)

        result_ls.append(zenkaku)
        tag.append(l[1])
    print ("NO of records ",k)
    result_rows = []
    train=[]
    
    for k in range(len(result_ls)):
        
        train.append([ result_ls[k], tag[k] ])
            
   


with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(train)



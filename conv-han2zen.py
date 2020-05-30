import sys
import csv
#import mojimoji
import random
args = sys.argv

with open(args[1]) as f:
    ls=[]
    reader = csv.reader(f, delimiter='\t')
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
        
        #print (str(k)+'\n')
        #print (l)
        zenkaku=l[0].translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
        print (zenkaku)
        print (l[0])
        print (l[1])
        #kk=l[0].replace('\\r','')
        #kk=kk.replace('\\n','')
        #lstr=l[0].encode('utf-8')
        #result_strs = mojimoji.han_to_zen(lstr,ascii=False)

        result_ls.append(l[0])
        tag.append(l[1])
    print ("NO of records ",k)
    result_rows = []
    train=[]
    
    for k in range(len(result_ls)):
        
        train.append([ result_ls[k], tag[k] ])
            
   


with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(train)



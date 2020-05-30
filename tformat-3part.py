import sys
import csv
import mojimoji
import random
args = sys.argv

with open(args[1]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]

    result_ls = []
    tag=[]
    k=0
    for l in ls:
#        print(mojimoji.han_to_zen(l[0],ascii=False))
#        print(mojimoji.han_to_zen(l[0])
        k+=1
        #print (str(k)+'\n')
        #print (l[0]+';'+l[1])
        #lstr=l[0].encode('utf-8')
        #result_strs = mojimoji.han_to_zen(l[0],ascii=False)

        result_ls.append(l[0])
        tag.append(l[1])

    result_rows = []
    train=[]
    test=[]
    eve=[]
    kk=[]
    still=True
    pp=0
    next=0
    print (len(result_ls))
    t100=len(result_ls)-1
    t70=int(len(result_ls)*0.8)
    print (t70)
    t15=int(len(result_ls)*0.1)
    print (t15)
    
    while(still):
        pp+=1
        k=random.randint(1,len(result_ls)-1)
        if (k in kk):
            #print ("exist")
            continue
        else:
            kk.append(k)
            result_rows.append([ result_ls[k], tag[k] ])
            #print (str(k)+'\n')
            #print (result_ls[k]+'\t'+tag[k] )
            if (next==0):
                train.append([result_ls[k],tag[k]])
            elif (next==1):
                test.append([result_ls[k],tag[k]])
            elif (next==2):
                eve.append([result_ls[k],tag[k]])                

        if (len(kk)>t70):
            print (len(kk))
            next=1
        if (len(kk)>(t70+t15)):
            print (len(kk))
            next=2
        if (len(kk)>=t100 or pp>500000000):
            print (pp)
            still=False
   

dr=args[2]
trainf=dr+"/train.tsv"
testf=dr+"/test.tsv"
devf=dr+"/dev.tsv"
with open(trainf, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(train)
with open(testf, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(test)
with open(devf, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(eve)


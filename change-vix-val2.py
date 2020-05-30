import sys
import csv
#import mojimoji

args = sys.argv

with open(args[1]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]

    result_ls = []
    tags=[]
    ii=0
    limit=20000
    for l in ls:
        if (ii<limit):
#        print(mojimoji.han_to_zen(l[0],ascii=False))
#        print(mojimoji.han_to_zen(l[0]))
        #result_strs = mojimoji.han_to_zen(l[0])
            #print (len(l[0]))
            result_ls.append(l[0])
            tag=l[1]
            if (float(tag)<0):
                value='0'
            else:
                value='1'
            tags.append(value)
            ii+=1
        else:
            break
    print (ii)

    
#    print(result_ls)
#    print(result_ls[0])

    result_rows = []
    print (len(result_ls))
    for i in range(len(result_ls)):
#        print('[{}][{}]'.format(result_ls[i],ls[i][1]))

        result_rows.append([ result_ls[i], tags[i]])
        
    #print(result_rows)
#    print(result_rows[0])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)

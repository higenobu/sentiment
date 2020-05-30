import sys
import csv
#import mojimoji

args = sys.argv

with open(args[1]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]

    result_ls = []
    ii=0
    limit=10
    for l in ls:
        if (ii<limit):
#        print(mojimoji.han_to_zen(l[0],ascii=False))
#        print(mojimoji.han_to_zen(l[0]))
        #result_strs = mojimoji.han_to_zen(l[0])
            print (len(l[0]))
            result_ls.append(l[0])
            ii+=1
        else:
            break
    
#    print(result_ls)
#    print(result_ls[0])

    result_rows = []

    for i in range(limit):
#        print('[{}][{}]'.format(result_ls[i],ls[i][1]))

        result_rows.append([ result_ls[i], ls[i][1] ])
        
    #print(result_rows)
#    print(result_rows[0])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)
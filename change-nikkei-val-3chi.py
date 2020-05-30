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
    limit=5000000
    for l in ls:
        if (ii<limit):

            result_ls.append(l[0])
            tag=l[1]
            #set 0 if minus set 1 if positive
            print (tag)
            if (float(tag)<-1):
                value='1'
            elif (float(tag)>1):
                value='2'
            else:
                value='0'
            tags.append(value)
            ii+=1
        else:
            break
    print (ii)

    


    result_rows = []
    print (len(result_ls))
    for i in range(len(result_ls)):


        result_rows.append([ result_ls[i], tags[i]])
        


with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)
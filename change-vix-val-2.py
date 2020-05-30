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
            #if (abs(float(tag))<1.0):
            if (float(tag)<0):
                value='0'
            else:
                value='1'
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
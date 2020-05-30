#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
import sys

args = sys.argv

#with open(args[1]) as f:
#    reader = csv.reader(f, delimiter=';')
file=open(args[1])

f=open(args[2],mode='w')
'''
nw=[]
#tag={'':'','0':'A','1':'B','2':'C','3':'D','4':'E'}
#tag={'0':'0','1':'1','2':'C','3':'D','4':'E'}
news=f2.readline()

i=0
while (news):
	#print (news)
	nw.append(news)
	news=f2.readline()
	i+=1

kk=i
'''
memo=file.readline()
nw=[]
i=0
s=0
ff=0
kk=50000
while (memo):
	#print (memo)
	if (i>=kk):
		break
	
	mem=memo.split('\t')
	if (mem):
		tag=mem[1]
		mm1=mem[0]
		
	if (mm1 in nw):
		s+=1
		#print ("DUP:"+mm1)
		memo=file.readline()
		i+=1
		continue
	else:
		#print (mm1)
		nw.append(mm1)
		ff+=1

		wmm1=mm1.replace('"','')
		wmm1=wmm1.replace("'",'')
		wmm1=wmm1.replace(",",'')
		wmm1=wmm1.replace(".",'')
		wmm1=wmm1.replace("\\n",'')
		wmm1=wmm1.replace("\\r",'')
		aa=wmm1.find('datePublished:')
		if (aa):
			cont=wmm1[0:aa]
		else:
			cont=wmm1[:]
		#cont=cont.strip()
		#print (mm0+";"+cont)

		f.write(cont+'\t'+tag+'\n')
		memo=file.readline()
		i+=1
	

print ("duplicate"+str(s))
print ("district"+str(ff))
print ("total"+str(i))
file.close()
f.close()
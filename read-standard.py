#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jaconv
import sys

args = sys.argv

#with open(args[1]) as f:
#    reader = csv.reader(f, delimiter='\t')
file=open(args[1])

f2=open(args[2])
f=open(args[3],mode='w')
nw=[]
tag={'':'','0':'A','1':'B','2':'C','3':'D','4':'E'}
tagab=['A','B']
#tag={'0':'0','1':'1','2':'C','3':'D','4':'E'}
#read news
news=f2.readline()

i=0
while (news):
	#print (news)
	nw.append(news)
	news=f2.readline()
	i+=1

kk=i
#read result id
memo=file.readline()
#mmeo=file.readline()
i=0
s=0
ff=0
a=0
f.write("NO  datatag  correct predict same content"+'\n')
while (memo):
	print (memo)
	if (i>=kk):
		break
	#one record is missing from result +1
	cont=nw[i+1]
	ww=cont.split('\t')
	#print (ww[1])
	#print (memo)
	wws=ww[1].strip()
	#wws=wws.replace('\r','')
	# mms[0] is pred mms[1] is original
	mms=memo.split('=')
	if (mms):
		mm0=mms[0].strip()
		mm1=mms[1].strip()
		tag0=tag[str(mm0)]
		tag1=tag[str(mm1)] 
	if (tag0==tag1):
		s+=1
		same='s'
		if (tag0 in tagab):
			a+=1
	else:
		same=' '
		ff+=1
	f.write(str(i)+';'+wws+';'+tag1+';'+tag0+';'+same+';'+cont+'\n')
	memo=file.readline()
	i+=1
	#print (i)
	if (i>1000):
		break
print ("total of content: ",kk)
print ("total of output score: ",i)
print ("correct:"+str(s))
print ("wrong:"+str(ff))
print ("AB:"+str(a))
file.close()
f.close()
f2.close()
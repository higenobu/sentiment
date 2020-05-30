#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jaconv

file=open('/tmp/news-22-random/log.txt')
f2=open('/tmp/news-22-random/dev.tsv')
f=open('/home/ubuntu/log/news-22-random-r',mode='w')
nw=[]
tag={'':'','0':'A','1':'B','2':'C','3':'D','4':'E'}
#tag={'0':'0','1':'1','2':'C','3':'D','4':'E'}
news=f2.readline()
#news=f2.readline()
i=0
while (news):
	#print (news)
	nw.append(news)
	news=f2.readline()
	i+=1

kk=i

memo=file.readline()
#memo=file.readline()
i=0
s=0
ff=0
f.write("NO  datatag  correct predict same content"+'\n')
while (memo):
	print (memo)
	cont=nw[i+1]
	ww=cont.split('\t')
	#print (ww[1])
	#print (memo)
	wws=ww[1].strip()
	#wws=wws.replace('\r','')
	memo=memo.strip()
	if (memo):
		mm0=memo[0]
		mm1=memo[2]
		tag0=tag[mm0]
		tag1=tag[mm1] 
	if (tag0==tag1):
		s+=1
		same='s'
	else:
		same=' '
		ff+=1
	f.write(str(i)+';'+wws+';'+tag1+';'+tag0+';'+same+';'+cont+'\n')
	memo=file.readline()
	i+=1
	#print (i)
	if (i>500):
		break
print ("total of content ",kk)
print ("total of output score ",i)
print ("correct"+str(s))
print ("wrong"+str(ff))
file.close()
f.close()

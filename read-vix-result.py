#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
import sys

args = sys.argv

#with open(args[1]) as f:
#    reader = csv.reader(f, delimiter='\t')
file=open(args[1])

f2=open(args[2])
f=open(args[3],mode='w')
nw=[]
#tag={'':'','0':'A','1':'B','2':'C','3':'D','4':'E'}
#tagab=['A','B']
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
b=0
e=0
f.write("seq-no, correct, predict, same, content"+'\n')
while (memo):
	#print (memo)
	if (i>=kk):
		break
	#one record is missing from result +1
	cont=nw[i+1]
	ww=cont.split('\t')
	#print (ww[1])
	#print (memo)
	wcont=ww[0].strip()
	wws=ww[1].strip()
	#wws=wws.replace('\r','')
	# mms[0] is pred mms[1] is original
	mms=memo.split('=')
	if (mms):
		mm0=mms[0].strip()
		mm1=mms[1].strip()
		#no tag
		tag0=float(mm0)
		tag1=float(mm1)
	
	if (abs(tag0-tag1)<0.1):
		e+=1
		same='-'
	if (tag0==1):
		b+=1
		same='+'
	if (tag0==2):
		a+=1
		same='*'
	
	if (tag0==0):
		s+=1
		same='<'

	else:
		same=' '
		ff+=1
	f.write(str(i)+','+mm1+','+mm0+','+same+','+wcont+'\n')
	memo=file.readline()
	i+=1
	#print (i)
	if (i>100000):
		break
p0=args[3]+","
p1="totalnews:"+str(kk)
p2=",totalscore:"+str(i)
p3=",correct score:"+str(e)
p4=", 0=,"+str(s)
p5=", 1=,"+str(b)
p6=", 2=,"+str(a)
p7=",0:%,"+str(float(s/i))[0:4]
p8=", 1:%,"+str(float(b/i))[:4]
p9=",2:%,"+str(float(a/i))[0:4]

p10=",correct:%,"+str(float(e/i))[0:4]
#wstrw=",total of content:"+str(kk)+ ";e="+str(e)+";0="+str(s)+";2="+str(a)+";1="+str(b)+";2%="+str(float(a/i))+";1%="+str(float(b/i))+";0%="+str(float(s/i))
wstrw=p0+p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
print (wstrw)
f.write(wstrw+'\n')

file.close()
f.close()
f2.close()
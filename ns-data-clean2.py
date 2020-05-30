#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
#https://pypi.org/project/jaconv/
#import pandas as pd
import sys
import csv
#import mojimoji

args = sys.argv



def check (i):

	if '\u3040'<=i<='\u309F' or '\u30A0'<=i<='\u30FF' or '\u0030'<=i<='\u0039' or '\u0041'<=i<='\u005A' or '\u0061'<=i<='\u007A' or '\u3000'<=i<='\u303F' or  '\u4e00'<=i<='\u9fff' or '\uFF00'<=i<='\uFFEF' or '\u0000'<=i<='\u007F':

		return True
	else:
		return False

def han2zen(han):
	ZEN = "".join(chr(0xff01 + i) for i in range(94))
	HAN = "".join(chr(0x21 + i) for i in range(94))

	ZEN2HAN = str.maketrans(ZEN, HAN)
	HAN2ZEN = str.maketrans(HAN, ZEN)
	return han.translate(HAN2ZEN)
# 全角から半角
	#print(ZEN.translate(ZEN2HAN))
# 結果
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

# 半角から全角
	#print(HAN.translate(HAN2ZEN))

#ZEN = "".join(chr(0xff01 + i) for i in range(94))
#HAN = "".join(chr(0x21 + i) for i in range(94))

'''
upper = dict((0xFF21 + ch, 0x0041 + ch) for ch in range(26))
lower = dict((0xFF41 + ch, 0x0061 + ch) for ch in range(26))
number= dict((0xFF10 + ch, 0x0030 + ch) for ch in range(10))

with open(args[1]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]

    result_ls = []
    jj=0
    for l in ls:
    	jj+=1
    	print (l[0])
    	for w in l[0]:
    		if (check(w)):
    			print (w)
    		else:
    			print ("NO:")
    	if (jj>1):
    		break

    	#print(han2zen(l[0]))
        #print(mojimoji.han_to_zen(l[0],ascii=False))
        #print(mojimoji.han_to_zen(l[0]))
#        result_strs = mojimoji.han_to_zen(l[0])

#        result_ls.append(result_strs)



#data = pd.read_csv('/home/medex/nlpnews/ns22-vix.csv', encoding='utf-8')
file=open('/home/medex//nlpnews/ns22-vix.csv',encoding = "ISO-8859-1")
#f=open('ns-22-vix-clean.csv',mode='w')
#ww=file.readline()
#ww="アラブ諸国・地域の協力機構のアラブ連盟は１日、トランプ米大統領が発表した中東和平"

for w in data:
	if (check(w)):
		print (w)
	else:
		print ("NO:")

'''
#,encoding = "ISO-8859-1"
file=open(args[1])

#f2=open(args[2])
f=open(args[2],mode='w')
#file=open('/home/medex/nlpnews/ns22-vix.csv')
#f=open('ns-22-vix-clean.csv',mode='w')

memo=file.readline()
i=0
while (memo):
	i+=1
	#if (i>1):
	#	break
	print (memo.strip())
	mm=memo.split('\t')
	
	flag=mm[1]
	kk=mm[0]
	#kk=kk.decode('utf-8')
	
	kk=kk.replace('▽','')
	#　◇
	kk=kk.replace('◇','')
	kk=kk.replace('【','')
	#【
	kk=kk.replace('【','')
	
	kk=kk.replace(',','')
	kk=kk.replace('\\r','')
	kk=kk.replace('\\n','')
	aa=kk.find('datePublished:')
	if (aa):
		mk=kk[0:aa]
	
	
	#umk=mk.decode('utf-8')
	
	
	

	
		#print mk
		#umk=mk.decode('utf-8')

		#zmk=jaconv.h2z(umk)
		#ymk=zmk.encode('utf-8')
		#print (ymk)
		#zmk=han2zen(mk)
	f.write(mk+'\t'+flag+'\n')
	memo=file.readline()
	i+=1
	print (i)
	if (i>10000):
		break


file.close()
f.close()

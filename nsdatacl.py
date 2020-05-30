#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
#https://pypi.org/project/jaconv/
#import pandas as pd
import sys
import csv
import argparse

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



def nsdatacl(news,addnews):
	file=open(news)
	f=open(addnews,mode='w')

	memo=file.readline()
	i=0
	while (memo):
		i+=1
	
		print (memo.strip())
		mm=memo.split(';')
	
		flag='1'
		kk=mm[1]
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
		f.write(mk+'\t'+flag+'\n')
		memo=file.readline()
		i+=1
		print (i)
		if (i>50000):
			break


	file.close()
	f.close()

if __name__=='__main__':
  parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument(
      'news',
      help='news')
  parser.add_argument(
      'addnews',
      help='addnews')
    
    
  args = parser.parse_args()
    
  nsdatacl(args.news,args.addnews)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import jaconv
import sys
import argparse


#args = sys.argv

#with open(args[1]) as f:
#    reader = csv.reader(f, delimiter=';')
def  removedups(news,addnews):
	file=open(news)

	f=open(addnews,mode='w')
	memo=file.readline()
	nw=[]
	i=0
	s=0
	ff=0
	kk=500000
	while (memo):
	#print (memo)
		if (i>=kk):
			break
		memo=memo.strip()
		mem=memo.split('\t')
		if (len(mem)<2):
			print ("Bad format data")
			memo=file.readline()
			i+=1
			continue			
		if (len(mem)==2):
			

			tag=mem[1]
			mm1=mem[0]
		if (mm1=='' or mm1==None):
			print ("NO data")
			memo=file.readline()
			i+=1
			continue			
		
		if (mm1 in nw):
			s+=1
		
			memo=file.readline()
			i+=1
			continue
		else:
		
			nw.append(mm1)
			ff+=1
			f.write(mm1+'\t'+tag+'\n')
			memo=file.readline()
			i+=1
	

	print ("duplicate no:"+str(s))
	print ("district no:"+str(ff))
	print ("total:"+str(i))
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
    
  removedups(args.news,args.addnews)

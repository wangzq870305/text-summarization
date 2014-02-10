#! /usr/bin/env python
#coding=utf-8
from __future__ import division
import numpy as ny
import math

def cosine(source,target):
    numerator=sum([source[word]*target[word] for word in source if word in target])
    sourceLen=math.sqrt(sum([value*value for value in source.values()]))
    targetLen=math.sqrt(sum([value*value for value in target.values()]))
    denominator=sourceLen*targetLen
    if denominator==0:
        return 0
    else:
        return numerator/denominator

def PageRank(documents):    
    #document-to-document transfer matrix
    dd=ny.zeros((len(documents),len(documents)))
    for i,source in enumerate(documents):
        # p(w|d)
        for j,target in enumerate(documents):
	    dd[i,j]=cosine(source.words,target.words)
    
    for i,source in enumerate(documents):
        # p(w|d)
        sumJ=sum([dd[i,j] for j in range(len(documents))])
        for j,target in enumerate(documents):
	    if sumJ>0:
		dd[i,j]/=sumJ
	    else:
		dd[i,j]=0
    
    Y=[0]*len(documents)
    for i,l in enumerate(documents):
        Y[i]=1
    
    # PageRank
    # pr=0.15+0.85*sum(pr[j]*link[i,j])
    for t in range(10):
        tY=[0]*len(documents)
        for i in range(len(documents)):
            tY[i]=0.15+0.85*sum([dd[j,i]*Y[j] for j in range(len(documents)) if i!=j])  
        Y=tY
        
        print t
    
    results=[(y,i) for i,y in enumerate(Y)]

    results.sort()
    results.reverse()
    return [result[1] for result in results]


def PageRank1(documents):    
    #document-to-document transfer matrix
    dd=ny.zeros((len(documents),len(documents)))
    for i,source in enumerate(documents):
        # p(w|d)
        for j,target in enumerate(documents):
	    dd[i,j]=cosine(source.words,target.words)
    
    for i,source in enumerate(documents):
        # p(w|d)
        sumJ=sum([dd[i,j] for j in range(len(documents))])
        for j,target in enumerate(documents):
	    if sumJ>0:
		dd[i,j]/=sumJ
	    else:
		dd[i,j]=0
    
    Y=[0]*len(documents)
    for i,l in enumerate(documents):
        Y[i]=1
    
    # PageRank
    # pr=0.15+0.85*sum(pr[j]*link[i,j])
    for t in range(10):
        tY=[0]*len(documents)
        for i in range(len(documents)):
            tY[i]=0.15+0.85*sum([dd[j,i]*Y[j] for j in range(len(documents)) if i!=j])  
        Y=tY
        
        print t
    
#    results=[(y,i) for i,y in enumerate(Y)]
#
#    results.sort()
#    results.reverse()
    return Y

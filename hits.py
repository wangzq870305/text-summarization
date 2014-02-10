#! /usr/bin/env python
#coding=utf-8
from __future__ import division
import numpy as ny
import math

def HITS(documents): 	    
    words=[]
    for document in documents:
        words+=document.words.keys()
    words=[word for word in set(words)]
    
    wi=dict([(word,i) for i,word in enumerate(words)])
    
    T={}
    for i,document in enumerate(documents):
        T[i]={}
        for word in document.words:
            T[i][wi[word]]=document.words[word]
            
    Auth=[1]*len(documents)
    Hub=[1]*len(words)
    
    for t in range(10):
        tAuth=[0]*len(documents)
        for i in range(len(Auth)):
            tAuth[i]=sum([T[i][j]*Hub[j] for j in T[i]])
            
        for j in range(len(Hub)):
            Hub[j]=sum([T[i][j]*Auth[i] for i in range(len(Auth)) if j in T[i]])
        
        Auth=[a/sum(tAuth) for a in tAuth]
        Hub=[h/sum(Hub) for h in Hub]
        
        print t
    
    results=[(y,i) for i,y in enumerate(Auth)]

    results.sort()
    results.reverse()
    return [result[1] for result in results]
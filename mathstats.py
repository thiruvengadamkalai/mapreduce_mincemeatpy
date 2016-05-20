#!/usr/bin/env python
import mincemeat
from sys import argv

script, text = argv
file = open(text,'r')
data = list(file)
file.close()

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

count = 0
summ = 0
std = 0.00
r = 0
mn = 0.00


def mapfn(k, v):
    for w in v.split():

        yield 'result' , int(w)



def reducefn(k, vs):  
     import math
#     count = len(vs)
#     summ = sum(vs)
#     mn= summ/count
     count = 0
     summ = 0
     std = 0.00
     r = 0
     mn = 0.00
     for i in vs:
        count = count + 1;
        summ = summ + i;

     mn = summ / count
     for i in vs:
        r = r + ((i - mn)**2)        

     std = math.sqrt(r/count) 
     resultlist = []
     resultlist.append(('count:',count))
     resultlist.append(('sum:',summ))
     resultlist.append(('standard deviation:',std))
     print resultlist	
     return resultlist


s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

#resultlist = []


 #resultlist.append((k,results[k]))

print  results

#print results

#resultlist = []
#resultlist.append(('sum',results[1]))

#print resultlist


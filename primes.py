#!/usr/bin/env python
import mincemeat

#data = range(1, 100, 2)

data = {}
for i in range(1,10000000):
   data[i] = i

#print datasource[3]
#count = 0

  
def mapfn(k, v):

     def isprime(n):
       if n == 1:
          return False
       if n == 2 or n == 3:
          return True
       elif (n % 2 == 0) or (n % 3 == 0):
          return False
       i = 5
       while i*i <= n:
          if (n % i == 0) or (n % i+2 == 0):
             return False
          i = i + 6
       return True
   
        
     def ispal(n):
       if (str(n) == str(n)[::-1]):
           return True
       else: 
           return False
           
        
     n = v
     palprime = []
       
     if isprime(n) and ispal(n):  
        palprime = palprime + [n] 
        yield 'num' , palprime
        


def reducefn(k, vs):  

    return vs


s = mincemeat.Server()
s.datasource = data
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print  results


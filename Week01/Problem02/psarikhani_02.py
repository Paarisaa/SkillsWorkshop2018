# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 00:56:23 2018

@author: paris
"""

smaller=1
bigger=2
list_fibo=[]

while bigger<4000000:
    if bigger%2==0:
        list_fibo.append(bigger)
        
    new=smaller+bigger
    smaller=bigger
    bigger=new
        
print(sum(list_fibo))
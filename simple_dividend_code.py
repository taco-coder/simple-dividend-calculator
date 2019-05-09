# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print ('Hello world')

initial = float(input("Initial investment?"))
dividend = float(input("Yearly dividend yield?"))
monthly = float(input("Monthly contribution?"))

years = int(input("Number of years?"))

for iter in range(1, years + 1):
   initial *= (1 + dividend/100)
   initial += monthly * 12
   #.format is used to give the initial 2 decimal places
   print ("Year %d:{0:.2f}".format(initial) % iter)

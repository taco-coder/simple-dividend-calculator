# -*- coding: utf-8 -*-
"""
Spyder Editor

This file simply takes an initial investment, a yearly yield, a monthly contribution, 
and a number of years to print out a persons ROI. 

Author:Tahwab Noori
Date:May 9, 2019
"""
import os


initial = float(input("Initial investment?"))
dividend = float(input("Yearly dividend yield?"))
monthly = float(input("Monthly contribution?"))

years = int(input("Number of years?"))

for iter in range(1, years + 1):
   initial *= (1 + dividend/100)
   initial += monthly * 12
   #.format is used to give the initial 2 decimal places
   print ("Year %d:{0:.2f}".format(initial) % iter)
os.system("pause")

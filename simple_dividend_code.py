# -*- coding: utf-8 -*-
"""
This file simply takes an initial investment, a yearly yield, a monthly contribution, 
and a number of years to print out a persons ROI. Finds monthly returns and accounts for 
reinvestment increases at given intervals

Author:Tahwab Noori
Date:May 9, 2019
"""
import os

def dynamic(years, monthly, initial):
    value = str(input("Would you like the option of increasing your monthly contributions after some months? (y/n)"))
    if(value == 'y'):
        increase = int(input("How many times a year would you like to increase your monthly contributions?"))
        reinvest = float(input("How much would you like to increase your contribution by each time?"))
        for iter in range(1, years + 1): #how many years of investing
            #loop finds the return each month
            #after some interval, the reinvestment amount increases
            for i in range (0, increase):
                for j in range (1, int(12 / increase) + 1):
                    initial *= (1 + (dividend / 12) /100)
                    initial += monthly
                    #.format is used to give the initial 2 decimal places                
                    print ("End of month %d:${0:.2f}".format(initial) % (j + (i * (12 / increase))))
                #reinvestment amount increases
                monthly += reinvest
                print('Investment increased: ' + str(reinvest))
                print('Current reinvestment amount: ' + str(monthly))
            print ("End of year %d:${0:.2f}".format(initial) % iter)
    elif(value == 'n'):
        for iter in range(1, years + 1): #how many years of investing
            initial *= (1 + (dividend) /100)
            if iter != 1:
                initial += monthly * 12
            #.format is used to give the initial 2 decimal places
            print ("End of year %d:${0:.2f}".format(initial) % iter)
    else:
        print("Error: invalid input. Please try again.")
        dynamic()

    

initial = float(input("Initial investment?"))


dividend = float(input("Yearly dividend yield?"))

monthly = float(input("Monthly contribution?"))

years = int(input("Number of years?"))
'''
Uncomment these to use set values for easier debugging
years = 10
dividend = 7.8
initial = 10000
#monthly = 100
'''
dynamic(years, monthly, initial)

    
        
    
#prevents script from closing if running in Windows CMD prompt
os.system("pause")

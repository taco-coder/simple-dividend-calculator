# -*- coding: utf-8 -*-
"""
This file simply takes an initial investment, a yearly yield, a monthly contribution, 
and a number of years to print out a persons ROI. Finds monthly returns and accounts for 
reinvestment intervals at given intervals

Author:Tahwab Noori
Date:May 9, 2019
"""
import os
import time

initial = float(input("Initial investment?"))
dividend = float(input("Yearly dividend yield?"))
monthly = float(input("Monthly contribution?"))
years = int(input("Number of years?"))

#noReinvest takes the years, monthly, initial, and dividend float values and 
#calculates the users yearly returns at that fixed rate
def noReinvest(years, monthly, initial, dividend):
     output = fileMaker()
     for iter in range(1, years + 1): #how many years of investing
            initial *= (1 + (dividend) /100)
            if iter != 1:
                initial += monthly * 12
            #.format is used to give the initial 2 decimal places
            print ("End of year %d:${0:.2f}".format(initial) % iter)
            output.write("End of year %d:${0:.2f}\n".format(initial) % iter)
     output.close()

#reinvest takes years, monthly, initial, dividend, interval and reinvest then calculates users
#yearly returns while also increasing the reinvestment rate at user-defined intervals. Also prints out
#monthly returns for more precise investing goals.
def reinvest(years, monthly, initial, dividend):
     
     interval = int(input("How many times a year would you like to interval your monthly contributions?"))
     reinvest = float(input("How much would you like to interval your contribution by each time?"))      
     value = str(input("Would you like to print out monthly returns as well?(y/n)"))
     output = fileMaker()
     #for loop with nested loop to 
     for iter in range(1, years + 1): #how many years of investing
            #loop finds the return each month
            #after some interval, the reinvestment amount increases
            for i in range (0, interval):
                
                for j in range (1, int(12 / interval) + 1):
                    
                    initial *= (1 + (dividend / 12) /100)
                    initial += monthly
                    #.format is used to give the initial 2 decimal places                
                    if(value == 'y' or 'Y'):
                        print("End of month %d:${0:.2f}".format(initial) % (j + (i * (12 / interval))))
                        output.write("End of month %d:${0:.2f}".format(initial) % (j + (i * (12 / interval))))
                #reinvestment amount increases
                monthly += reinvest
                
                print('Investment interval: ' + str(reinvest))
                output.write('Investment interval: ' + str(reinvest))
                print('Current reinvestment amount: ' + str(monthly))
                output.write('Current reinvestment amount: ' + str(monthly))
                
            print("End of year %d:${0:.2f}".format(initial) % iter)
            output.write("End of year %d:${0:.2f}".format(initial) % iter)
     output.close()

def fileMaker():
    val = str(input("Would you like to save your data to a textfile?(y/n)"))
    if(val == 'y' or 'Y'):
        currentPath = os.getcwd()
        #checks if directory currently exists and creates directory if it doesn't.
        if(os.path.exists(currentPath + '/output_files') == False):
            outputPath = os.makedirs(currentPath + '/output_files')
        else:
            outputPath = currentPath + '/output_files'
            os.chdir(outputPath) 
        if len(os.listdir(outputPath)) == '0':
            currentTime = time.strftime("%Y_%m_%d@%Hh%Mm%Ss")
            output = open("output-%s.txt" % currentTime, 'w')
        else:
            value = str(input("There currently exists a previous savefile. Would you like to overwrite or create a new save file?\n(O = overwrite/C = create new file)"))
            if (value == 'c' or 'C'):
                currentTime = time.strftime("%Y_%m_%d@%Hh%Mm%Ss")
                output = open("output-%s.txt" % currentTime, 'w')
            elif(value == 'o' or 'O'):
                 for iter in os.listdir(outputPath):
                     print('%d-' % iter)
        return output

#dynamic sets the values for all the args and params then calls the appropriate functions based on the users input
def dynamic():
    value = str(input("Would you like the option of increasing your monthly contributions after some months? (y/n)"))
    
    if(value == 'y'):       
        reinvest(years, monthly, initial, dividend)         
    elif(value == 'n'):      
        noReinvest(years, monthly, initial, dividend)       
    else: #if user makes an invalid selection, runs dynamic again
        print("Error: invalid input. Please try again.")
        dynamic()
        
#start
dynamic()
os.system("pause") #prevents script from closing if running in Windows CMD prompt

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
currentTime = time.strftime("%Y_%m_%d@%Hh%Mm%Ss")

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
     outfile = fileMaker()
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
                        outfile.write("End of month %d:${0:.2f}".format(initial) % (j + (i * (12 / interval))))
                #reinvestment amount increases
                monthly += reinvest
                
                print('Investment interval: ' + str(reinvest))
                outfile.write('Investment interval: ' + str(reinvest))
                print('Current reinvestment amount: ' + str(monthly))
                outfile.write('Current reinvestment amount: ' + str(monthly))
                
            print("End of year %d:${0:.2f}".format(initial) % iter)
            outfile.write("End of year %d:${0:.2f}".format(initial) % iter)
     outfile.close()
#fileMaker asks the user if they would like to save the data to a textfile.
#it checks if the the appropriate directory exists and creates it if necessary. It gives the user the option
#of overwriting an existing save file or creating a new file, respectivly. Calls the fileOverWriter function for overwriting.
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
            output = open("output-%s.txt" % currentTime, 'w')
        else:
            control = False
            while(control == False):
                option = str(input("There currently exists some previous savefile(s). Would you like to overwrite or create a new save file?\n(O = overwrite/C = create new file)"))
                if (option == "c"):
                    control = True
                    output = open("output-%s.txt" % currentTime, 'w')
                elif(option == "o"):
                    control = True
                    output = open(fileOverWriter(outputPath), 'w')
                else:
                    print("Invalid input. Please try again.")
        return output
#fileOverWriter takes the outputPath of the folder containing the output files and prints them to the user.
#The user then chooses a file from the list to overwrite. The file is respectively renamed and the newly named file is returned.
def fileOverWriter(outputPath):
    outputList = os.listdir(outputPath)
    
    for iter in range(len(outputList)):
        print('%d-' % iter + outputList[iter] + '\n')
    indexValue = False
    while indexValue == False:
        numfile = int(input("Please pick which number file.(eg 1, 2, 3, etc.)"))
        try:
            indexValue = True
            overwriteFile = outputList[numfile]
            newName = "output-%s.txt" % currentTime
            os.rename(overwriteFile, newName)
        except IndexError:
            print("Invalid input. That file index does not exist. Please try again.")
    return newName
        
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

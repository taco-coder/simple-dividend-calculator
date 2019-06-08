# -*- coding: utf-8 -*-
"""
This file simply takes an initial investment, a yearly yield, a monthly contribution, 
and a number of years to print out a persons ROI. Finds monthly returns and accounts for 
reinvestment intervals at given intervals

Author:Tahwab Noori
Date:May 9, 2019
"""
import os, time, requests, bs4



currentTime = time.strftime("%Y_%m_%d@%Hh%Mm%Ss")
#userValues gets the users input values for the variables.s
def userValues():
     initial = float(input("Initial investment?"))     
     monthly = float(input("Monthly contribution?"))
     years = int(input("Number of years?"))
     return initial, monthly, years
 
#noReinvest takes the years, monthly, initial, and dividend float values and 
#calculates the users yearly returns at that fixed rate
def noReinvest(initial, dividend, monthly, years):

     outfile = fileMaker()
     if(outfile != None):
         for iter in range(1, years + 1): #how many years of investing
             initial *= (1 + (dividend) /100)
          
             initial += monthly * 12
                 #.format is used to give the initial 2 decimal places
             print ("End of year %d:${0:.2f}".format(initial) % iter)
             outfile.write("\n\nEnd of year %d:${0:.2f}\n\n\n".format(initial) % iter)
         outfile.close()
     elif(outfile == None):
         for iter in range(1, years + 1): #how many years of investing
             initial *= (1 + (dividend) /100)
             
             initial += monthly * 12
                 #.format is used to give the initial 2 decimal places
             print ("End of year %d:${0:.2f}".format(initial) % iter)
                         
#reinvest takes years, monthly, initial, dividend, interval and reinvest then calculates users
#yearly returns while also increasing the reinvestment rate at user-defined intervals. Also prints out
#monthly returns for more precise investing goals.
def reinvest(initial, dividend, monthly, years):

     interval = int(input("How many times a year would you like to increase your monthly contributions?"))
     reinvest = float(input("How much would you like to increase your contribution by each time?"))      
     value = str(input("Would you like to print out monthly returns as well?(y/n)"))
     
     outfile = fileMaker()
     if(outfile != None):
         #for loop with nested loop to 
         for iter in range(1, years + 1): #how many years of investing
             #after some interval, the reinvestment amount increases
             for i in range (0, interval):
                 #loop finds the return each month
                 for j in range (1, int(12 / interval) + 1):
                     
                     initial *= (1 + (dividend / 12) /100)
                     initial += monthly
                     #.format is used to give the initial 2 decimal places   
                     #endOfMonths is used to calculate what the current month is based on the amount of times the 12 months are broken up into intervals.                     
                     endOfMonths = j + (i * (12 / interval))
                     if(value == 'y'):
                         print("End of month %d:${0:.2f}".format(initial) % (j + (i * (12 / interval))))
                         outfile.write("End of month %d:${0:.2f}\n".format(initial) % (j + (i * (12 / interval))))
                         
                         print('Current reinvestment amount: ' + str(monthly))
                         outfile.write('Current reinvestment amount: ' + str(monthly) + '\n')
                     if(endOfMonths == 12):
                         print("End of year %d:${0:.2f}\n".format(initial) % iter)
                         outfile.write("\n\nEnd of year %d:${0:.2f}\n\n\n".format(initial) % iter)
                 #end of current interval
                 monthly += reinvest

         outfile.close()
     elif(outfile == None):
          #for loop with nested loop to 
         for iter in range(1, years + 1): #how many years of investing             
             #after some interval, the reinvestment amount increases
             for i in range (0, interval):
                 #loop finds the return each month
                 for j in range (1, int(12 / interval) + 1):
                     
                     initial *= (1 + (dividend / 12) /100)
                     #.format is used to give the initial 2 decimal places 
                     #endOfMonths is used to calculate what the current month is based on the amount of times the 12 months are broken up into intervals.
                     #multiplied by current interval. eg adds X months times the ith interval to the current month
                     endOfMonths = j + (i * (12 / interval))
                     if(value == 'y' or 'Y'):
                         print("End of month %d:${0:.2f}".format(initial) % (j + (i * (12 / interval))))                         
                         print('Current reinvestment amount: ' + str(monthly))
                     if(endOfMonths == 12):
                         print("End of year %d:${0:.2f}".format(initial) % iter)
                 #end of current interval
                 monthly += reinvest
                 #checks if it reaches the complete end of all the months and years. Doesn't print out the 'increased' statement at the end of the program
                 if(endOfMonths != 12 and iter != years):
                     print('Investment increased: ' + str(reinvest))
            
#fileMaker asks the user if they would like to save the data to a textfile.
#it checks if the the appropriate directory exists and creates it if necessary. It gives the user the option
#of overwriting an existing save file or creating a new file, respectivly. Calls the fileOverWriter function for overwriting.
def fileMaker():
    
    val = str(input("Would you like to save your data to a textfile?(y/n)"))
    
    if(val == 'y'):
        currentPath = os.getcwd()
        #checks if directory currently exists and creates directory if it doesn't.
        if(os.path.exists(currentPath + '\output_files') == False):
            outputPath = os.makedirs(currentPath + '\output_files')
        else:
            outputPath = currentPath + '\output_files'
            os.chdir(outputPath) 
        if (len(os.listdir(outputPath)) == 0):
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
    elif(val == 'n'):
        return None
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
def dynamic(initial, dividend, monthly, years):
    value = str(input("Would you like the option of increasing your monthly contributions after some months? (y/n)"))
    
    if(value == 'y'):       
        reinvest(initial, dividend, monthly, years)         
    elif(value == 'n'):      
        noReinvest(initial, dividend, monthly, years)       
    else: #if user makes an invalid selection, runs dynamic again
        print("Error: invalid input. Please try again.")
        dynamic()
        
def searchDividend():
    value = str(input("Do you want to search a specific ticker for your dividend calculation? (y/n)"))
    if(value == 'n'):
        initial, monthly, years = userValues()
        dividend = float(input("Yearly dividend yield?"))
        dynamic(initial, dividend, monthly, years)
    elif(value == 'y'):
        initial, monthly, years = userValues()       
        dividend = googleDividend()
        dynamic(initial, dividend, monthly, years)

def googleDividend():
    ticker = str(input("Please enter the ticker you would like to search for. (AAPl, KO, DIS, BABA, etc.)"))
    searchResult = requests.get("https://www.nasdaq.com/symbol/" + ticker)
    searchResult.raise_for_status()
    searchText = bs4.BeautifulSoup(searchResult.text, 'html.parser')
    searchMain = searchText.select(".column > .table-table")[1].select(".table-row > .table-cell")

    for iter in range(0, len(searchMain)):
        tableText = searchMain[iter].text.replace(" ", "").replace("\n", "")
        if(tableText == "CurrentYield"):
            divText = searchMain[iter + 1].text.replace(" ", "").replace("\n", "").replace("%", "")
            return float(divText)

    
#start
searchDividend()
os.system("pause") #prevents script from closing if running in Windows CMD prompt

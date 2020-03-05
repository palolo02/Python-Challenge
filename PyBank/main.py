# ===============================================
# Paolo Vega
# 03/02/2020
# Version 1.0
#   Version 1.1   03/03/2020
# File to run the PyBank analysis of the financial records of our company
# ===============================================

# Add required modules to facilitate the implementation
import os
import csv
import datetime
import statistics

folder =  "C:\\Users\\Paolo\\Bootcamp\\Python-Challenge\\Resources"
csvName = "budget_data.csv"
csvpath = os.path.join(folder,csvName)
# Lists to store key and values
months = []
profits = []
incprofits = []

totalValue = 0
noMonths = 0
avgChange = 0

greatestIncrease = 0
greatestIncMonth = ""
greatestDecrease = 0
greatestDecMonth = ""


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)   
    
    for row in csvreader:
        months.append(row[0])
        profits.append(float((row[1])))

#initialize variables
i = 1
while i < (len(profits)):
    incTemp = profits[i]-profits[i-1]
    incprofits.append(incTemp)
    if(incTemp > greatestIncrease):
        greatestIncrease = incTemp
        greatestIncMonth = months[i]
    if(incTemp < greatestDecrease):
        greatestDecrease = incTemp
        greatestDecMonth = months[i]
    i += 1

avgChange = statistics.mean(incprofits)
totalValue = sum(profits)
noMonths = len(months)

print("Financial Analysis")
print("----------------------------------------------")
print(f"Total months:  {noMonths}")
print(f"Total value: {totalValue:,.3f} ")
print(f"Average: $ {avgChange:,.3f}")
print(f"Greatest increase in Profit: {greatestIncMonth} , $ {greatestIncrease:,.3f}")
print(f"Greatest decrease in Profit: {greatestDecMonth} , $ {greatestDecrease:,.3f}")

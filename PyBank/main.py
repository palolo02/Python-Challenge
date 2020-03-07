# ===============================================
# Paolo Vega
# Bootcamp Data Analytics
# Version   1.0.0 03/02/2020
#           1.0.1 03/04/2020
#           1.0.2 03/05/2020
#           1.0.3 03/06/2020
# File to run the PyBank analysis of the financial records of our company
# ===============================================

# Add required modules to facilitate the implementation
import os
import csv
import datetime
import statistics

# Define the folder and file name location
folder = 'PyBank'
csvName = "budget_data.csv"
csvpath = os.path.join(folder,csvName)

# Lists that will store the months, profits and the highest increase
months = []
profits = []
incprofits = []

# initialize variables
totalValue = 0
noMonths = 0
avgChange = 0

# Descriptions for the greaates increase and greatest decrease
greatestIncrease = 0
greatestIncMonth = ""
greatestDecrease = 0
greatestDecMonth = ""

# Open and read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Store the header to avoid column names
    header = next(csvreader)

    # Go through each line to create two lists for holding months and their profit
    for row in csvreader:
        months.append(row[0])
        profits.append(float((row[1])))

# Calculate the differences each month with respect the previous one to 
# identify the profit increases
# iterate from the second row to the last one
for i in range(1,(len(profits))):
    # Calculate the increase
    incTemp = profits[i]-profits[i-1]
    # Add the difference to the increase values
    incprofits.append(incTemp)

    # Assess whether this increase is the highest increase among the dataset
    if(incTemp > greatestIncrease):
        greatestIncrease = incTemp
        greatestIncMonth = months[i]

    # Assess whether this increase is the highest decrease among the dataset
    if(incTemp < greatestDecrease):
        greatestDecrease = incTemp
        greatestDecMonth = months[i]

# Calculate the totals of the months and their profit of the differences
avgChange = statistics.mean(incprofits)
totalValue = sum(profits)
noMonths = len(months)

# Print results with appropiate format
print("Financial Analysis")
print("----------------------------------------------")
print(f"Total months:  {noMonths}")
print(f"Total value: {totalValue:,.3f} ")
print(f"Average: $ {avgChange:,.3f}")
print(f"Greatest increase in Profit: {greatestIncMonth} | $ {greatestIncrease:,.3f}")
print(f"Greatest decrease in Profit: {greatestDecMonth} | $ {greatestDecrease:,.3f}")

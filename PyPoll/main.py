# ===============================================
# Paolo Vega
# 03/02/2020
# Version 1.0
#   Version 1.1 03/04/2020
# File to run the PyPoll analysis
# ===============================================

# Add required modules to facilitate the implementation
import os
import csv
import datetime
import statistics

folder =  "C:\\Users\\Paolo\\Bootcamp\\Python-Challenge\\Resources"
csvName = "election_data.csv"
csvpath = os.path.join(folder,csvName)

candidates = []
results = []
percentages = []
totalVotes = 0
noVotes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)


    for row in csvreader:
        totalVotes += 1
        try:
            results[candidates.index(row[2])] += 1
        except ValueError:
            candidates.append(row[2])
            results.append(0)    

for candidate in candidates:
    percentages.append( (results[candidates.index(candidate)] / totalVotes)*100 )

print("Election Results")
print("----------------------------------------------")
print(f"Total Votes:  {totalVotes:,}")
print("----------------------------------------------")

winner = 0
for candidate in candidates:
    index = candidates.index(candidate)
    print(f"{candidates[index]}: , {percentages[index]:.1f}% ({results[index]:,})")
    if (percentages[index] > percentages[winner]):
        winner = index

print("----------------------------------------------")
print(f"Winner:  {candidates[winner]}")
print("----------------------------------------------")

# Create text file





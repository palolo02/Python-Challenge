# ===============================================
# Paolo Vega
# Bootcamp Data Analytics
# Version   1.0.0 03/02/2020
#           1.0.1 03/04/2020
#           1.0.2 03/05/2020
#           1.0.3 03/06/2020
# File to run the PyPoll analysis
# ===============================================

# Add required modules
import os
import csv
import datetime
import statistics

# Define the folder and file name location
folder = 'PyPoll'
csvName = "election_data.csv"
# Define the output file name
txtName = "results.txt"
csvpath = os.path.join(folder,csvName)

# Lists that will store the candidates, their votes and the percentages for each
candidates = []
votes = []
percentages = []
# Total number of votes in the dataset
totalVotes = 0

# Open and read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Store the header to avoid column names
    header = next(csvreader)

    # Go through each line to count the votes and get the candidates names
    for row in csvreader:
        totalVotes += 1
        # Try to get see if the candidate is already in the list to count his votes,
        # otherwise we need add it first and start from 0
        try:
            votes[candidates.index(row[2])] += 1
        except ValueError:
            candidates.append(row[2])
            votes.append(0)    

# Calculate the percentage of votes for each candidate
for candidate in candidates:
    percentages.append( (votes[candidates.index(candidate)] / totalVotes)*100 )

# Print the results
print("Election Results")
print("----------------------------------------------")
print(f"Total Votes:  {totalVotes:,}")
print("----------------------------------------------")
# Determine who is the winner according to the highest percentage of votes
winner = 0
for candidate in candidates:
    # Identify the candidate based on an index
    index = candidates.index(candidate)
    # Print the results with format of number (separate with commas and decimal point)
    print(f"{candidates[index]}: {percentages[index]:.1f}% ({votes[index]:,})")
    # Assess whether we are identifying the winner
    if (percentages[index] > percentages[winner]):
        winner = index
# Print the winner among the candidates
print("----------------------------------------------")
print(f"Winner:  {candidates[winner]}")
print("----------------------------------------------")

# Create text file to write and open it for writing purposes
resultFile =  open(os.path.join(folder,txtName), "w")
# Same format as in the terminal
resultFile.writelines("Election votes\n")
resultFile.writelines("----------------------------------------------\n")
resultFile.writelines(f"Total Votes:  {totalVotes:,} \n")
resultFile.writelines("----------------------------------------------\n")
# Print the information for each candidate
for candidate in candidates:
    # Get the position for each candidate and print votes and percentages with appropiate format
    index = candidates.index(candidate)
    resultFile.writelines(f"{candidates[index]}: {percentages[index]:.1f}% ({votes[index]:,}) \n")
resultFile.writelines("----------------------------------------------\n")
resultFile.writelines(f"Winner:  {candidates[winner]} \n")
resultFile.writelines("----------------------------------------------\n")
# Close the file
resultFile.close()






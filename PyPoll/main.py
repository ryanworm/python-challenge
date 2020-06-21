import os
import csv

file_path = os.path.join("Resources", "PyPoll.csv")

#set variables to hold the lists
voterID = []
county = []
candidate = []

#set, read file path
with open(file_path) as csvfile:
    row_data = list(csv.reader(csvfile, delimiter=','))
    
#open the file to write
analysisPath = os.path.join("Analysis", "PyPoll_analysis.txt")
outFile = open(analysisPath, "w")

#append lists
for row in row_data:
    voterID.append(row[0])
    county.append(row[1])
    candidate.append(row[2])

#remove first row containing headers from data list
del voterID[0], candidate[0], county[0] 

#calc & print num votes
numvotes = len(voterID)
print(f'\nElection Results')
outFile.write(f'Election Results\n')
print(f'-------------------------')
outFile.write(f'-------------------------\n')
print(f'Total Votes: {numvotes}')
outFile.write(f'Total Votes: {numvotes}\n')
print('-------------------------')
outFile.write(f'-------------------------\n')

# create list of candidates
list_of_candidates = set(candidate)

#set var to hold votes
votes_per_can = []
percent_per_can = []
winner = []
printcount = 0

#calc votes for candidates
for i in list_of_candidates:
    votes_per_can.append(candidate.count(i))
    percent_per_can.append(candidate.count(i)/ numvotes *100)
    print(f'{i}: {votes_per_can[printcount]} {percent_per_can[printcount]:.2f}')
    outFile.write(f'{i}: {votes_per_can[printcount]} {percent_per_can[printcount]:.2f}\n')
    printcount += 1

#get winner
for i in list_of_candidates:
    if (candidate.count(i) == max(votes_per_can)):
        winner.append(i)
#in case of ties
if len(winner) > 1:
    print(f'TIE: {winner}')
    outFile.write(f'TIE: {winner}\n')
    print(f'-------------------------')
    outFile.write(f'-------------------------\n')
else:
    print(f'-------------------------')
    outFile.write(f'-------------------------\n')
    print(f'WINNNER: {winner[0]}')
    outFile.write(f'WINNNER: {winner[0]}\n')
    print(f'-------------------------\n')
    outFile.write(f'-------------------------\n')

outFile.close()


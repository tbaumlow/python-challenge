# Import required modules / libraries
import os
import csv

# Get the data from the resource file
election_data = os.path.join('.', 'Resources', 'election_data.csv')

# Define the Candidates vote metrics (percent and count)
Candidates = []
CandidateVotes = []
CandidatePercent = []
TotalVotesCast = 0

# Open the source data file
with open(election_data, "r", newline = "") as VoteFile:
    VoteReader = csv.reader(VoteFile, delimiter = ",")
    ColumnHeaders = next(VoteReader)
    ColumnNumbers = range(len(ColumnHeaders))
    
    # Create loop to run through all the rows of data
    for row in VoteReader:
        
        # rows to fields
        IDNumber = row[0]
        County = row[1]
        Candidate = row[2]
                
        # total counter increment
        TotalVotesCast += 1 

        # If candidate is not in arrray, add the candidate
        if Candidate not in Candidates:
            Candidates.append(Candidate)
            CandidateIndex = Candidates.index(Candidate)
            CandidateVotes.append(0)
            
        # get candidate position / index 
        else:
            CandidateIndex = Candidates.index(Candidate)
            
        # vote count increment for candidate
        CandidateVotes[CandidateIndex] += 1
    
    # Calculate the percentage of votes each candiate received 
    for Votes in CandidateVotes:
        WorkPercent = (Votes/TotalVotesCast) * 100
        WorkPercent = "%.3f%%" % WorkPercent
        CandidatePercent.append(WorkPercent)
    
    # Find the candidate who won the most votes
    VoteWinner = max(CandidateVotes)
    VoteWinnerIndex = CandidateVotes.index(VoteWinner)
    Winner = Candidates[VoteWinnerIndex]

# Display the result
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(TotalVotesCast)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(CandidatePercent[i])} ({str(CandidateVotes[i])})")
print("--------------------------")
print(f"Winner: {Winner}")
print("--------------------------")

# Write results in text file
outputpath = os.path.join(".", "analysis", "results.txt")
output = open(outputpath, "w")
output.write("--------------------------\n")
output.write(str(f"Total Votes: {str(TotalVotesCast)}\n"))
for i in range(len(Candidates)):
    line = str(f"{Candidates[i]}: {str(CandidatePercent[i])} ({str(CandidateVotes[i])})\n")
    output.write(line)
output.write("--------------------------\n")
output.write(str(f"Winner: {Winner}\n"))
output.write("--------------------------\n")

output.close()

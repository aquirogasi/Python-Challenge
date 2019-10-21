
import os
import csv
import pandas as pd

# Path to collect data from the Resources folder
paypall_csv = os.path.join('..', 'python-challenge', 'election_data.csv')

# Use Pandas to read data
election_data_file_pd = pd.read_csv(paypall_csv)


# Find the total number of votes cast using the value_counts method in Voter ID column
total_votes = election_data_file_pd["Voter ID"].count()

# Find a complete list of candidates who received votes
candidate_list_with_votes = election_data_file_pd["Candidate"].unique()

# Find the total number of votes each candidate won
votes_count_by_candidate = election_data_file_pd["Candidate"].value_counts()

# Find the percentage of votes each candidate won
percentage_of_votes = votes_count_by_candidate / total_votes


# Find the winner of the election
winner = max(votes_count_by_candidate.keys(),key =(lambda k: votes_count_by_candidate[k]))

# Open a text file with w+ which indicates write and create a file if it does not exist in library
file = open("pay_pall.txt","w+")

# Print and write results
print('Election Results')
file.write('Election Results \n')
print('--------------------------')
file.write('-------------------------- \n')
print(f'Total Votes: {total_votes}')
file.write(f'Total Votes: {total_votes} \n')

# Loop through the merged list (zip used) to print the last but one results in just one line           
for cand_with_votes,votes_by_candidate,percentage_of_votes in zip(candidate_list_with_votes,votes_count_by_candidate,percentage_of_votes):
    
    print(f"{cand_with_votes} : {'{:.3%}'.format(percentage_of_votes)} ({votes_by_candidate})")
    file.write(f"{cand_with_votes} : {'{:.3%}'.format(percentage_of_votes)} ({votes_by_candidate}) \n")

print(f"Winner: {winner}")
file.write(f'Winner: {winner} \n')

           
# Closing the file      
file.close()
           









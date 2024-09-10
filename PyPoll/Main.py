import os
import csv

votes = 0

candidate_list = []
candidate_votes = {}
winner = ""
winner_votes = 0
results = ""

# path to accept data from resources folder
#csvpath = os.path.join('Resources', 'election_data.csv') unable to locate the folder with this code-help from ChatGPT for the following code:
pypoll_csvpath = '/Users/thule/OneDrive/Desktop/Data Analysic certificate/python_challenge/PyPoll/Resources/election_data.csv'

# read csv file
with open(pypoll_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

# total number of votes cast
    for row in csvreader:
        votes +=1

# list of condidates
with open(pypoll_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

    for row in csvreader:
        can = row[2]

        if can not in candidate_list:
            candidate_list.append(can)

# calculate count and percentage of votes each candidate recieved 
    
with open(pypoll_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

    for row in csvreader:
        can = row[2]
        if can in candidate_votes:
            candidate_votes[can] += 1
        else:
            candidate_votes[can] = 1

    for can in candidate_list:
        vote = candidate_votes[can]
        perc_votes = (vote / votes) * 100
        results += f"{can} : {perc_votes:.3f}% ({vote})\n"

# winner
        if vote > winner_votes:
            winner = can
            winner_votes = vote
    print(f"{winner}")
    
    # print final election results
       
    print("Election Results")
    print("--------------------------------")
    print(f'Total Votes: {votes}')
    print("--------------------------------")
    print(results)
    print("--------------------------------")
    print(f'Winner: {winner}')

# output text file results to analysis folder
#output_file = os.path.join('Analysis', 'Election_Results.txt') unable to locate the folder with this code-help from ChatGPT for the following code:
output_file = '/Users/thule/OneDrive/Desktop/Data Analysic certificate/python_challenge/PyPoll/Analysis/Election resutls.txt'
with open(output_file, 'w') as txtfile:
    results_file = csv.writer(txtfile)
    results_file.writerow(["Election Results"])
    results_file.writerow(["--------------------------------"])
    results_file.writerow(['Total Votes: {votes}'])
    results_file.writerow(["--------------------------------"])
    results_file.writerow([results])
    results_file.writerow(["--------------------------------"])
    results_file.writerow([f'Winner: {winner}'])

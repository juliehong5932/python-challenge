#create file path
import os

#import csv file
import csv


candidates =[]
vote_counts = []
max_vote =[]


total_votes = 0
candidate = 0
max_vote = 0
vote_counts = 0

#define csv path
csvpath = os.path.join('Resources', 'election_data.csv')



#open csv file
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)



#total number of votes
    for row in csvreader:
        total_votes = total_votes + 1
        
        #candidate vote
        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1

                
        else:
            candidates.append(candidate)
        



#winner

winner = max(vote_counts)



#output

print(f'Election Results')
print(f'----------------------')
print(f'Total Votes: {total_votes}')
print(f'----------------------')
# for count in range(len(candidates)):
#     print(f'{candidate[count]}:{percentage[count]}% ({vote_counts[coundt]})')
# print(f'----------------------')
# print(f'Winner: {winner}')
# print(f'----------------------')


#text file
with open('PyPoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'----------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'----------------------', file=text_file)
    # for count in range(len(candidates)):
    #     print(f'{candidate[count]}:{percentage[count]}% ({vote_counts[coundt]})', file=text_file)
    # print(f'----------------------', file=text_file)
    # print(f'Winner: {winner}', file=text_file)
    # print(f'----------------------', file=text_file)

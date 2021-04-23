import csv
import os
#Libraries and csv path
csv_path = os.path.join('Resources','election_data.csv')

data = []
voterin_number = 0
namein_list = []
vote_counts = {}


with open(csv_path) as file:
    reader = csv.reader(file)

    header = next(reader)
    #print(header)

    for row in reader:
        data.append(row)

#print(data[0])
voterin_number = len(data)
#print(voterin_number)

for row in data:
    if row[2] not in namein_list:
        namein_list.append(row[2])

#print(namein_list)

for n in range(0, len(namein_list)):
    #creates a dictionary with each candidate's vote count, starting at 0
    vote_counts[namein_list[n]] = 0
#print(vote_counts)

for row in data:
    #matches the dictionary and adds 1 per vote
    current_number = vote_counts[row[2]]
    current_number += 1
    vote_counts[row[2]] = current_number

#print(vote_counts)

#winner selector
winner = ''
high = 0
for n in namein_list:
    if vote_counts[n] > high:
        high = vote_counts[n]
        winner = n
print(winner)

print("Election Results\n-------------------")
print(f"Total Votes : {voterin_number}\n---------------------")
for n in namein_list:
    #str function included to use the brackets to extract first parts
    print(f"{n}: {str(100*vote_counts[n]/voterin_number)[0:5]}% ({vote_counts[n]})")
print("-------------------")
print(f"Winner: {winner}\n---------------------")
    










        




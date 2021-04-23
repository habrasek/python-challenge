#PyBank Script by Harlan Brasek

import csv
import os
#Libraries and csv path
csv_path = os.path.join('Resources','budget_data.csv')

number_of_months = 0
net_total = 0
average_change = 0
big_loss = 0
big_gain = 0
data_list = []

with open(csv_path) as file:
    csvreader = csv.reader(file, delimiter =',')

    """
    Used code to see if there was a header
    so that I could get an accurate number of months
    """
    csv_header = next(csvreader)
    print(csv_header)
#puts all of the data in a list so
#I don't have to make a bunch of with opens

    for row in csvreader:
        data_list.append(row)

#Makes it so I don't have to call int everytime
for row in data_list:
    row[1] = int(row[1])

#print(data_list)

number_of_months = len(data_list)
#print(number_of_months)

for row in data_list:
    net_total += row[1]
#print(net_total)

total_change = 0
for number in range(1,number_of_months):
    total_change += (data_list[number][1]- data_list[number-1][1])
#print(total_change)
average_change = total_change/number_of_months
#print(average_change)

for row in data_list:
    if row[1] > big_gain:
        big_gain = row[1]

#print(big_gain)

for row in data_list:
    if row[1] < big_loss:
        big_loss = row[1]

time_of_loss = ''
time_of_gain = ''

for row in data_list:
    if row[1] == big_loss:
        time_of_loss = row[0]
    if row[1] == big_gain:
        time_of_gain = row[0]
#print(time_of_gain)
#print(time_of_loss)

#print(big_loss)

print("Financial Analysis\n-----------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: {time_of_gain} {big_gain}")
print(f"Greatest Decrease: {time_of_loss} {big_loss}")



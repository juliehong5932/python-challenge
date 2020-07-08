#create file path
import os

#import csv file
import csv

#objectives
date = []
net_profit =[]
profit_change =[]
total_change =[] 
greatest_increase_date = []
greatest_increase =[]
greatest_decrease_date = []
greatest_decrease =[]


#variables
total_months = 0
net_profit = 0
profit_change = 0
previous_period = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0


#define csv path
csvpath = os.path.join('Resources', 'budget_data.csv')



#open csv file
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)


#Total Number of months

    for row in csvreader:
        total_months = total_months + 1
        date.append(row[0])
      
#Net total of profit/losses
        net_profit += int(row[1])
        

#Average change
        profit_change = int(row[1]) - previous_period
        previous_period = int(row[1])
        total_change += int(profit_change)    
        average_change = round(total_change/total_months, 2)   

    


#Greatest Increase in profit
        if profit_change > greatest_increase:
                greatest_increase_date = row[0]
                greatest_increase = profit_change
        

#Greatest Decrease in profits
        if profit_change < greatest_decrease:
                greatest_decrease_date = row[0]
                greatest_decrease = profit_change

#output

print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {len(date)}')
print(f'Total: $ {net_profit}')
print(f'Average Change:$ {average_change} ')
print(f'Greatest Increase in Profits: {greatest_increase_date}, ${greatest_increase}')
print(f'Greatest Decrease in Losses: {greatest_decrease_date}, ${greatest_decrease}')


#Print(f'Greatest Decrease in Profits: {date},')

#text file
with open('PyBank.txt', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'------------------', file=text_file)
    print(f'Total Months: {len(date)}', file=text_file)
    print(f'Total: $ {net_profit}', file=text_file)
    print(f'Average Change:$ {average_change}', file=text_file)
    print(f'Greatest Increase in Profits: {greatest_increase_date}, ${greatest_increase}', file=text_file)
    print(f'Greatest Decrease in Losses: {greatest_decrease_date}, ${greatest_decrease}', file=text_file)

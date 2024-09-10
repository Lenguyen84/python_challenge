import os
import csv

total_months = 0
total_amount = 0
greatest_increase = 0
greatest_decrease = 0
changes = []
dates = []

# path to accept data from resources folder
#csvpath = os.path.join('Resources','budget_data.csv') unable to locate the folder with this code-help from ChatGPT for the following code:
csvpath = '/Users/thule/OneDrive/Desktop/Data Analysic certificate/python_challenge/PyBank/Resources/budget_data.csv'

# read csv file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvreader) 
    
    # read each row after header
    for row in csvreader:
        
    # total months
        total_months +=1

# net total
with open(csvpath,'r') as csvfile:
    csv_header = next(csvfile)
    
    for row in csv.reader(csvfile):
        total_amount +=int(row[1])
        
# changes in profit/losses
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)  
    data = list(csvreader)

for i in range(1, total_months):
    current_profit = int(data[i][1])
    previous_profit = int(data[i-1][1])
    change = current_profit - previous_profit
    changes.append(change)
    dates.append(data[i][0])

# Used AI Xpert Learning Assistant to help pair date with greatest inc/dec   
# greatest increase/decrease in profits (date and amount)
    if change > greatest_increase:
        greatest_increase = change
        greatest_inc_date = data[i][0]
    elif change <greatest_decrease:
        greatest_decrease = change
        greatest_dec_date = data[i][0] 

# average change of profit/losses
average = sum(changes) / len(changes)

# greatest increase in profits (date and amount)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)  
    data = list(csvreader)
   
# print financial analysis
print("Finanancial Analysis")
print("--------------------------------")
print(f"Total Months: {total_months}") 
print(f"Total: ${total_amount}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_date}, ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_dec_date}, ${greatest_decrease}")

# output financial analysis to txt document in analysis folder
#output_file = os.path.join('Analysis','Financial Analysis.txt') unable to locate the folder with this code-help from ChatGPT for the following code:
output_file = '/Users/thule/OneDrive/Desktop/Data Analysic certificate/python_challenge/PyBank/Analysis/Financial Analysis.txt'

with open(output_file, 'w')as txtfile:
    results_file = csv.writer(txtfile)
    results_file.writerow(["Finanancial Analysis"])
    results_file.writerow(["--------------------------------"])
    results_file.writerow([f"Total Months: {total_months}"])
    results_file.writerow([f"Total: ${total_amount}"])
    results_file.writerow([f"Average Change: ${average:.2f}"])
    results_file.writerow([f'Greatest Increase in Profits: {greatest_inc_date}, ${greatest_increase}'])
    results_file.writerow([f'Greatest Decrease in Profits: {greatest_dec_date}, ${greatest_decrease}'])

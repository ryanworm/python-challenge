# import modules
import os
import csv

csvpath = os.path.join("Resources", "PyBank.csv")

# set lists
total = 0
months = 0
change_month = []
rev_change_list = []
max_change = ["",0]
min_change = ["",99999]

# opening the file using csv module
with open(csvpath, encoding='UTF-8') as csvfile:

# csv reader specifies delimiter and variable that holds contents
    csvreader= csv.reader(csvfile, delimiter=",")

#   get the header from the csv file
    csvheader=next(csvreader)
    
#   find opening values
    firstval=next(csvreader)
    #set value of month to 1 (first month)
    months = months + 1
    #'previous' will also have the value of total to give a reference value, and ensure that the 'difference' is 0
    rev_prev = int(firstval[1])

    for row in csvreader:
        #month count gets increased by 1
        months = months + 1
        #total is now equal to previous total plus revenue from current month
        total = total + rev_prev
    #net change is the difference between the previous month and the current month
        net_change = int(row[1]) - rev_prev
    #net previous is now equal to the current month's total, as this will be the 'previous' cell when compared to the next cell
        rev_prev = int(row[1])
    #to evaluate the month with the greatest change we need to keep a list of each change
        rev_change_list.append(net_change)
    #to track the month that the changes occur we also need to pytrack the months accordingly
        change_month.append(row[0])

        if net_change > max_change[1]:
            max_change[0]=row[0]
            max_change[1]=net_change

        if net_change < min_change[1]:
            min_change[0]=row[0]
            min_change[1]=net_change

month_average=sum(rev_change_list)/(len(rev_change_list))

print(f'\nFinancial Analysis')
print(f'--------------------------------')
print(f'Total Months: {months}')
print(f'Total ${total:.2f}')
print(f'Average Change: ${month_average:.2f}')
print(f'Greatest Increase in Profits: {max_change[0]} ${max_change[1]}')
print(f'Greatest Decrease in Profits: {min_change[0]} ${min_change[1]}')


#open the file to write
analysisPath = os.path.join("Analysis", "PyBank_analysis.txt")
with open(analysisPath, "w") as outFile:

    outFile.write(f'Financial Analysis')
    outFile.write(f'\n--------------------------------')
    outFile.write(f'\nTotal Months: {months}')
    outFile.write(f'\nTotal ${total:.2f}')
    outFile.write(f'\nAverage Change: ${month_average:.2f}')
    outFile.write(f'\nGreatest Increase in Profits: {max_change[0]} ${max_change[1]}')
    outFile.write(f'\nGreatest Decrease in Profits: {min_change[0]} ${min_change[1]}')
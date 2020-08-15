# import modules
import os
import csv

# pull the data set (csv file)
csvpath = os.path.join("PyBank.csv")

# set lists
total = 0
months = 0
change_month = []
net_change_list = []

# opening the file using csv module
with open(csvpath, encoding='UTF-8') as csvfile:

# csv reader specifies delimiter and variable that holds contents
    csvreader= csv.reader(csvfile, delimiter=",")

#   get the header from the csv file
    csvheader=next(csvfile)
    print(f'CSV Header:{csvheader}')

#   find opening values
    csvopen=next(csvfile)
    #set value of month to 1 (first month)
    months = months + 1
    #set the total value to the revenue of month 1
    total = total + int(row[1])
    #'previous' will also have the value of total to give a reference value, and ensure that the 'difference' is 0
    net_previous = int(row[1])

#   looping through rows
    for row in csvreader:
    #month count gets increased by 1
        months = months + 1
    #total is now equal to previous total plus revenue from current month
        total = total + int(row[1])
    #net change is the difference between the previous month and the current month
        net_change = int(row[1]) - net_previous
    #net previous is now equal to the current month's total, as this will be the 'previous' cell when compared to the next cell
        net_previous = int(row[1])
    #to evaluate the month with the greatest change we need to keep a list of each change
        net_change_list.append(net_change)
    #to track the month that the changes occur we also need to track the months accordingly
        change_month.append(row[0])

month_average=sum(net_change_list)/(change_month)
print(month_average)

#
#
# print(months)
# print(total)
# # add month
#         months.append(row[0])
#         # totalmonths = [str(month) for month in months]
#
#
# #    # add revenue
#         revenues.append(row[1])
#         print(revenues)
#         sum_revenue = sum(revenues)
#
#         # # finding average monthly revenue
        # def average(revenues):
        #     length_months = (len(months))
        #     total = 0.0
        #     for revenue in revenues:
        #         total = total + revenue
        #     return total / length_months
        # print(average([revenues]))
        # #
        #
        #
        #
        # # print(sum_rev)
# #
# #     # need to convert list to string to integer
#         revenue_string = ''.join(revenues)
#
#     # convert string to integer
    #     revenue_int = int(float(revenue_string))
     #   print(revenue_int)

    #test


        # totalrevenue = [int(revenue) for revenue in revenues]
    #     # sum_revenue = sum(totalrevenue)
    #     #
    #     print(sum_revenue)
    #     print(timeperiod)
    #     add month and rev
    #
    #     month_rev = {'totalmonths':'totalrevenue'}
    #     print(month_rev)
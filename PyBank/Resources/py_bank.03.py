# import modules

import os
import csv

# pull the data set (csv file)
bank_csv = os.path.join("PyBank.csv")

# set lists
total = 0
months = 0

# opening the file using csv module
with open(bank_csv, encoding='UTF-8') as csvfile:

# csv reader specifies delimiter and variable that holds contents
    csvreader= csv.reader(csvfile, delimiter=",")
    print(csvreader)
#
# #get the header from the csv file
    csv_header=next(csvfile)
    print(f'CSV Header:{csv_header}')
#
   #looping through rows
    for row in csvreader:
        months = months + 1
        total = total + int(row[1])

print(months)
print(total)
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
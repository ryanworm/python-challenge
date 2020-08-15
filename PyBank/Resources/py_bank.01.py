# import modules
import os
import csv

# pull the data set (csv file)
bank_csv = os.path.join("PyBank.csv")

#lists to store data
months = []
revenue = []
revenue_month = {months:revenue}

# opening the file
with open(bank_csv, encoding='utf-8') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    for row in csvreader:
    #add month
        months.append(row[0])
    #add revenue
        revenue.append(row[1])
        # print(len(months))
print (revenue_month)



    # read header row first
    # csv_header = next(csvfile)
    # print(f'Header:{csv_header}')

    # read through rows after header
    # for row in fileread:
    #     months = []
    #
    #     months = [row[0]]
    #     print(len(months))


# import modules

import os
import csv

# pull the data set (csv file)

bank_csv = os.path.join("PyBank.csv")

#lists to store data

months = []
moneys = []

# opening the file

with open(bank_csv, encoding='utf-8') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
    print(f'Header:{csv_header}')
    for row in csvreader:

    #add month

        months.append(row[0])
        total_months = len(months)
        print(total_months)

    # add revenue
    #need to convert list to string
        moneys.append(row[1])
        total_moneys = sum(moneys)
        print(total_moneys)
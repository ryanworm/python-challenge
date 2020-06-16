#import modules
import os
import csv

#prompt user to see what video they are looking for
video = input("What movie are you looking for?: ")

#set a path for the file
netflix_path = os.path.join("..", "netflix_lookup", "netflix_source_data.csv")

#Bonus Ex
#Set variable to check if we found the video

found = False

#open csv
with open (netflix_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #loop through looking for video
    for row in csvreader:
        if row[0] == video:
            print(row[0] + row [1] + "with a rating of " + row [5])

            #Bonus: set variable to confirm we have found the video
            found = True

            #bonus: stop at first restults to avoid duplicates
            break
    # if the video is never found, alert user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
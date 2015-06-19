# Convert data of scrobbles to tell about no. of plays during a time period.
import csv

with open('data/nickedes.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        # Todo: process datetime!
        print(row[2])

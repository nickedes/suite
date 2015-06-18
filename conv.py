# Purpose: Convert the csv(containing data about scrobbles) to a csv which has
#  only name of artists and it's count.
import csv

with open('data/nickedes.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    artists = {}
    for row in data:
        if row[0] not in artists:
            artists[row[0]] = 1
        else:
            artists[row[0]] += 1
with open('data/artists.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for data in artists:
        spamwriter.writerow([data, artists[data]])

with open('data/artists.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        print(', '.join(row))

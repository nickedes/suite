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
    avg = 0
    for data in artists:
        avg += artists[data]
    avg = avg//len(artists)
    print(avg)
with open('data/artists.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Artist", "count", "average"])
    for data in artists:
        if artists[data] >= avg:
            writer.writerow([data, artists[data], avg])

with open('data/artists.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        if row[1] >= row[2]:
            print(', '.join(row))

# Purpose: Convert the csv(containing data about scrobbles) to a csv which has
#  only name of artists and it's count.
import csv

with open('data/nickedes.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    artists = {}
    albums = {}
    for row in data:
        if row[0] not in artists:
            artists[row[0]] = 1
        else:
            artists[row[0]] += 1
        if row[1] not in albums:
            albums[row[1]] = 1
        else:
            albums[row[1]] += 1
    avg_artist = sum(artists.values())//len(artists)
    avg_album = sum(albums.values())//len(albums)
    print(albums)
with open('data/artists.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Artist", "count", "average"])
    for data in artists:
        if artists[data] >= avg_artist:
            writer.writerow([data, artists[data]])

with open('data/albums.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Album", "count"])
    for data in albums:
        if albums[data] >= avg_album:
            writer.writerow([data, albums[data]])

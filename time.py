# Convert data of scrobbles to tell about no. of plays during a time period.
import csv

time_dict = {}
with open('data/nickedes.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in data:
        i += 1
        if i != 1:
            try:
                ranges = row[3][11:row[3].index(':')] + "-" + str(int(row[3][11:row[3].index(':')])+1)
                if ranges not in time_dict:
                    time_dict[ranges]=1
                else:
                    time_dict[ranges]+=1
            except:
                pass
print(sum(time_dict.values()))
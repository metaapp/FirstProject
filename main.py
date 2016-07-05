print("This line will be printed.")

import csv
with open('c:\\Users\\Kubo\\Downloads\\20160108065157.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in csvreader:
        print(', '.join(row))

print("Skutocny koniec")
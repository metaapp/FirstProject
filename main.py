print("This line will be printed.")

import csv
import re
with open('c:\\Users\\Kubo\\Downloads\\20160108065157.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in csvreader:
        m = re.findall('(\d+)', row[0])
        print(m)

print("Skutocny koniec")
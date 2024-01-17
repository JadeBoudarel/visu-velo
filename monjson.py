from pprint import pprint
import csv
with open('parcours.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    all_datas = []
    for row in spamreader:
        my_line = {}
        my_line['x'] = row[0]
        my_line['y'] = row[3]
        all_datas.append(my_line)
    pprint(all_datas)
import csv

def problem3_7(csv_pricefile, flower):
    ifh = open(csv_pricefile,newline='')
    data = {}
    for line in csv.reader(ifh):
        data[line[0]] = line[1]
    print(data[flower])
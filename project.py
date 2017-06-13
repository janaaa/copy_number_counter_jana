#!/usr/bin/env python


import sys
import csv

#in_file = sys.argv[1]
in_file="C:\\Users\\xbieja\\Downloads\\Python\\Gains and losses.csv"
file = open(in_file, "r")

#open csv file
table = csv.reader(file, delimiter=',')

countMin = [0] * 10
countZero = [0] * 10
countPlus = [0] * 10

d = 0
for gene in table:
    i = 0
    if d > 0:
        for patient in gene:
            if len(patient) < 3:
                if patient == '-1':
                    countMin[i] += 1
                elif patient == '0':
                    countZero[i] += 1
                elif patient == '1':
                    countPlus[i] += 1
                i += 1
    d += 1
        
print(countMin)
print(countZero)
print(countPlus)
                
                
            

# for tum in len(table):
#     for row in table:
#         tumour = row[tum]
#         
    




#count all 1, -1, 0 
#def count(table):
    
    # if i == 1:
    #     gain = gain +1
    # elif i == -1:
    #     loss = loss +1
    # elif i == 0:
    #     neutral = neutal +1
    # else:
    #    #ignore
    # return 

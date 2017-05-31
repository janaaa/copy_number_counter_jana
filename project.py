#!/usr/bin/env python

import sys
import csv

#in_file = sys.argv[1]
in_file="C:\\Users\\xbieja\\Downloads\\Python\\Gains and losses.csv"
file = open(in_file, "r")

#open csv file
table = csv.reader(file, delimiter=',')

for row in table:
    print(row[0])




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

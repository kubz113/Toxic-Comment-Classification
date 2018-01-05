# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:16:59 2018

@author: jakub
"""

import csv


testData = []
toxicWords = set()
severeToxicWords = set()
obsceneWords = set()
threatWords = set()
insultWords = set()
identityHateWords = set()
 
with open('practiceData.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        copyRow = row[0:8]
        testData.append(copyRow)
        if row[2] == '1':
            for i in row[1].split():
                toxicWords.add(i)
        if row[3] == '1':
            for i in row[1].split():
                severeToxicWords.add(i)
        if row[4] == '1':
            for i in row[1].split():
                obsceneWords.add(i)        
        if row[5] == '1':
            for i in row[1].split():
                threatWords.add(i)                
        if row[6] == '1':
            for i in row[1].split():
                insultWords.add(i)
        if row[7] == '1':
            for i in row[1].split():
                identityHateWords.add(i)
                

toxicFile = open("toxicWords.csv",'w')
cw = csv.writer(toxicFile)
for i in toxicWords: 
    cw.writerow([i])  
toxicFile.close()

severeToxicFile = open("severeToxicWords.csv",'w')
cw = csv.writer(severeToxicFile)
for i in severeToxicWords: 
    cw.writerow([i])  
severeToxicFile.close()


obsceneFile = open("obsceneWords.csv",'w')
cw = csv.writer(obsceneFile)
for i in obsceneWords: 
    cw.writerow([i])  
obsceneFile.close()


threatFile = open("threatWords.csv",'w')
cw = csv.writer(threatFile)
for i in threatWords: 
    cw.writerow([i])  
threatFile.close()


insultFile = open("insultWords.csv",'w')
cw = csv.writer(insultFile)
for i in insultWords: 
    cw.writerow([i])  
insultFile.close()


identityHateFile = open("identityHateWords.csv",'w')
cw = csv.writer(identityHateFile)
for i in identityHateWords: 
    cw.writerow([i])  
identityHateFile.close()
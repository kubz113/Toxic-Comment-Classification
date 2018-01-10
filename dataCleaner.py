# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:16:59 2018

@author: jakub
"""

import csv
import pandas as pd


testData = []
toxicWords = set()
severeToxicWords = set()
obsceneWords = set()
threatWords = set()
insultWords = set()
identityHateWords = set()

df = pd.read_csv("train.csv")

for index, row in df.iterrows():
    if row['toxic'] == 1:
        for i in row['comment_text'].split():
            toxicWords.add(i)
    if row['severe_toxic'] == 1:
        for i in row['comment_text'].split():
            severeToxicWords.add(i)
    if row['obscene'] == 1:
        for i in row['comment_text'].split():
            obsceneWords.add(i)        
    if row['threat'] == 1:
        for i in row['comment_text'].split():
            threatWords.add(i)                
    if row['insult'] == 1:
        for i in row['comment_text'].split():
            insultWords.add(i)
    if row['identity_hate'] == 1:
        for i in row['comment_text'].split():
            identityHateWords.add(i)






toxicFile = open("toxicWords.csv",'w', encoding = 'utf-8', newline='')
cw = csv.writer(toxicFile)
cw.writerow(['words'])
for i in toxicWords: 
    cw.writerow([i])  
toxicFile.close()

severeToxicFile = open("severeToxicWords.csv",'w', encoding = 'utf-8', newline='')
cw = csv.writer(severeToxicFile)
cw.writerow(['words'])
for i in severeToxicWords: 
    cw.writerow([i])  
severeToxicFile.close()


obsceneFile = open("obsceneWords.csv",'w', encoding = 'utf-8', newline='')
cw = csv.writer(obsceneFile)
cw.writerow(['words'])
for i in obsceneWords: 
    cw.writerow([i])  
obsceneFile.close()


threatFile = open("threatWords.csv",'w', encoding = 'utf-8', newline='')
cw = csv.writer(threatFile)
cw.writerow(['words'])
for i in threatWords: 
    cw.writerow([i])  
threatFile.close()


insultFile = open("insultWords.csv",'w', encoding = 'utf-8', newline='')
cw = csv.writer(insultFile)
cw.writerow(['words'])
for i in insultWords: 
    cw.writerow([i])  
insultFile.close()


identityHateFile = open("identityHateWords.csv",'w', encoding = 'utf-8', newline='')
cw = csv.writer(identityHateFile)
cw.writerow(['words'])
for i in identityHateWords: 
    cw.writerow([i])  
identityHateFile.close()

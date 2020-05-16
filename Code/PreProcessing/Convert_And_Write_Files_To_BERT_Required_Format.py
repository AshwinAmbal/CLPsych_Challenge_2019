"""
Write files in BERT Required Format
"""


import random
import csv
req = list()
for i in range(1, 348):
    req.append(i)
req_final = random.sample(req,  35)
train_set = list()
dev_set = list()

with open("C:\\CLPsych Challenge\\Dataset\\PreProcessing\\User_Posts_Processed_Train.csv", 'r', encoding='utf8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for i, row in enumerate(reader):
        if(i == 0):
            header = row
        elif(i in req_final):
            dev_set.append(row)
        else:
            train_set.append(row)

full_train_set = train_set + dev_set

with open("C:\\CLPsych Challenge\\Dataset\\PreProcessing\\User_Posts_Processed_Train_Final.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',', quotechar = '"')
        writer.writerow(header)
        for row in train_set:
            writer.writerow(row)
            
with open("C:\\CLPsych Challenge\\Dataset\\PreProcessing\\User_Posts_Processed_Dev_Final.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',', quotechar = '"')
        writer.writerow(header)
        for row in dev_set:
            writer.writerow(row)

with open("C:\\CLPsych Challenge\\Dataset\\PreProcessing\\User_Posts_Processed_Train_Full_Final.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',', quotechar = '"')
        writer.writerow(header)
        for row in full_train_set:
            writer.writerow(row)


import pandas as pd
df = pd.read_csv('C:\\CLPsych Challenge\\Dataset\\PreProcessing\\User_Posts_Processed_Test.csv')
df.to_csv('C:\\CLPsych Challenge\\Dataset\\PreProcessing\\User_Posts_Processed_Test_Final.tsv', sep='\t', index=False, header=True)
# if you are creating test.tsv, set header=True instead of False

#df = pd.read_csv('C:\\CLPsych Challenge\\Temp\\train.csv', header=None)
#df.columns = ["id", "label", "a", "sentence"]
#df = df.drop(["label", "a"], axis=1)
#df.to_csv('C:\\CLPsych Challenge\\Temp\\test.tsv', sep='\t', index=False, header=True)
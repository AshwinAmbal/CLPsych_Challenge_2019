# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:50:46 2019

@author: AshwinAmbal
"""
import csv
path ="C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\crowd_train.csv"
file =open(path, 'r', encoding = 'utf8')
reader_data = csv.reader(file, delimiter=',')
user_label = list(reader_data)
all_user_id_label = dict()

for i, row in enumerate(user_label):
    if(i == 0):
        continue
    all_user_id_label[row[0]] = row[1]
    
path ="C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\task_C_train.posts.csv"
file = open(path, 'r', encoding = 'utf8')
reader_data = csv.reader(file, delimiter=',')

user_id_label = dict()

for i, row in enumerate(reader_data):
    if(i == 0):
        continue
    user_id_label[row[1]] = all_user_id_label[row[1]]
    

path ="C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\trainUserIds_TaskC_Final.csv"
with open(path, 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for key, value in user_id_label.items():
        writer.writerow([key, value])
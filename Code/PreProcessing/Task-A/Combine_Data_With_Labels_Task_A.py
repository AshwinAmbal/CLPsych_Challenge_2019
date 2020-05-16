"""
Combines various users involved in Task A with their respective labels
Input Files:
crowd_train.csv, task_A_train.posts.csv
Output Files:
trainUserIds_TaskA_Final.csv
"""

import csv

path = "C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\crowd_train.csv"
file = open(path, 'r', encoding='utf8')
reader_data = csv.reader(file, delimiter=',')
user_label = list(reader_data)
all_user_id_label = dict()

for i, row in enumerate(user_label):
    if (i == 0):
        continue
    all_user_id_label[row[0]] = row[1]

path = "C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\task_A_train.posts.csv"
file = open(path, 'r', encoding='utf8')
reader_data = csv.reader(file, delimiter=',')

user_id_label = dict()

for i, row in enumerate(reader_data):
    if (i == 0):
        continue
    user_id_label[row[1]] = all_user_id_label[row[1]]

path = "C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\trainUserIds_TaskA_Final.csv"
with open(path, 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    for key, value in user_id_label.items():
        writer.writerow([key, value])

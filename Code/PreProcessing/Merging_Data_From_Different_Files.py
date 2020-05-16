# -*- coding: utf-8 -*-
"""
Do an SQL join on the the dataset by joining on 'user_id', 'post_id' and 'subreddit'
"""

import pandas as pd

df1 = pd.read_csv("C:\\CLPsych Challenge\\Dataset\\clpsych19_test_data\\task_C_test.posts.csv")
df2 = pd.read_csv("C:\\CLPsych Challenge\\Dataset\\clpsych19_test_data\\shared_task_posts_test.csv")

merged_data = pd.merge(df1, df2, on=['post_id', 'user_id','subreddit'])

merged_data.to_csv("C:\\CLPsych Challenge\\Dataset\\clpsych19_test_data\\combined_data_Task_C_Test.csv", index=False, encoding='utf-8')

merged_data['user_id'].nunique()

df1 = pd.read_csv("C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\task_C_train.posts.csv")
df2 = pd.read_csv("C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\shared_task_posts.csv")

merged_data = pd.merge(df1, df2, on=['post_id', 'user_id','subreddit'])

merged_data.to_csv("C:\\CLPsych Challenge\\Dataset\\clpsych19_training_data\\combined_data_Task_C.csv", index=False, encoding='utf-8')

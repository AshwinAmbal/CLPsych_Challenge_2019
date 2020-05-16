# CLPsych_Challenge_2019
CLPsych_Challenge_2019 @ NAACL Conference. Link to paper: https://www.aclweb.org/anthology/papers/W/W19/W19-3022/

Read the paper attached above to understand the methodology

Read the Challenge given README for more info on the Challenge files

To reproduce numbers from paper above, use the preprocessed dataset folder in the following link which contains the full train data and the
challenge given set aside test set. Link here: https://www.dropbox.com/sh/vo9rfh793isptn1/AACTnvSzg5NwWTpJqwZzmBIta?dl=0

Separate source files were created for training and testing which look almost identical. Due to the lack of time neatness had to be compromised.
I apologize for the tardiness in advance :)

#### Source File Description
**Folder Descriptions**:\
Neural Network modelling: Contains all the BERT Training scripts\
PreProcessing: Contains all the scripts to prepare the data for input to BERT

**File Descriptions**:\
Files under **Neural Network Modelling**:\
All run_classifier_* files run the bert text classification code with task specific modification such as number of labels, etc\
Refer the BERT Tutorial for more info: https://github.com/md-labs/BERT_Tutorial

Files under **PreProcessing**:\
The Task A, Task B and Task C folders all contains similar files with the same intent but with minor changes specific to each task

I have described only one of the folders here (Task-A) but they apply to all files in other Task folders too.

**Combine_Data_With_Labels_Task_A.py**- Combines various users involved in Task A with their respective labels\
Input Files:\
crowd_train.csv, task_A_train.posts.csv\
Output Files:\
trainUserIds_TaskA_Final.csv, testUserIds_TaskA_Final.csv

**PreProcessing_User_Posts_Task_*.py**- Expands contractions, removes stopwords, etc and writes the posts in BERT required Input format\
Input Files:\
word_contractions_expansion.json, combined_data_Task_A.csv, trainUserIds_TaskA_Final.csv OR testUserIds_TaskA_Final.csv, task_A_train.posts.csv\
Output Files:\
User_Posts_Processed_Train.csv\
Similar Files: PreProcessing_User_Posts_Task_*.py

**PreProcessing_For_MIL_Task_*.py**- Expands contractions, removes stopwords, etc and writes the posts in a json files with key as user id and value as list of posts (=5)\
Input Files:\
word_contractions_expansion.json, combined_data_Task_A.csv, trainUserIds_TaskA_Final.csv OR testUserIds_TaskA_Final.csv, task_A_train.posts.csv\
Output Files:\
User_To_Posts.json\
Similar Files: PreProcessing_For_MIL_Test_Task_*.py

**Convert_And_Write_Files_To_BERT_Required_Format.py**- Write files in BERT Required Format

**Convert_Output_To_Reqd_Format.py**- Convert Output from BERT to Labels in Challenge

**Get_User_Embeddings_From_BERT.py**- For each user, get the embeddings from BERT for their respective posts. This code just retrieves the data from the Embeddings
json file that is written by BERT\
Similar File: Get_User_Embeddings_From_BERT_Test.py

**Merging_Data_From_Different_Files.py**- Do an SQL join on the the dataset by joining on 'user_id', 'post_id' and 'subreddit'

**Oversampling.py**- Oversampling Class B Samples to Class A

**Partitioning_Train_Data.py**- Splits the Full Train Data into Train-Test Sets and Oversampling the training data

**Read_CLS_Embeddings.py**- Read CLS Embeddings from extracted BERT Embeddings to train MIL

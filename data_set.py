import csv
import os
import pandas as pd
import random


rows = []
cwd = os.getcwd()

filename = "elitemarathoners.csv"
filepath = (cwd + "\\regroup\\" + filename)
with open(filepath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        actual_row = []
        actual_row.append(row[2])
        actual_row.append(row[4])
        actual_row.append(row[5])
        actual_row.append(row[-1])
        rows.append(actual_row)

filename = "nbaplayers.csv"
filepath = (cwd + "\\regroup\\" + filename)
with open(filepath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        actual_row = []
        actual_row.append(row[1])
        actual_row.append(row[5])
        actual_row.append(row[6])
        actual_row.append(row[-1])
        rows.append(actual_row)

filename = "yokozuna.csv"
filepath = (cwd + "\\regroup\\" + filename)
with open(filepath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        actual_row = []
        actual_row.append(row[1])
        actual_row.append(row[4])
        actual_row.append(row[5])
        actual_row.append(row[-1])
        rows.append(actual_row)

random.shuffle(rows)

ratio = int(len(rows) * 0.8)

model_train_data = rows[:ratio]
unseen_data = rows[ratio:-1]


filename = "data_set.csv"
filepath = (cwd + "\\regroup\\" + filename)
df = pd.DataFrame(model_train_data)
df.to_csv(filepath)

filename = "unseen_data_set.csv"
filepath = (cwd + "\\regroup\\" + filename)
df = pd.DataFrame(unseen_data)
df.to_csv(filepath)

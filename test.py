import pandas as pd

dataset1 = pd.read_csv("SE_rents2018_test1.csv")
dataset2 = pd.read_csv("SE_rents2018_test2.csv")
dataset3 = pd.read_csv("SE_rents2018_test3.csv")
dataTrain = pd.read_csv("SE_rents2018_train.csv")
print(dataset1.head())
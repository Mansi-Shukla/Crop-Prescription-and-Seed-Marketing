# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('seedmarket .csv', header = None)
transactions = []
for i in range(0, 47):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 16)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.28, min_confidence = 0.56, min_lift = 2, min_length = 5)

# Visualising the results
results = list(rules)
print(len(results))
print(results[0])
for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

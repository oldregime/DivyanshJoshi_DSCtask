

#Implement exploratory data analysis and gain an understanding of the data set and its features. 

import pandas as pd

# Load the data from the CSV file
data = pd.read_csv("slighted.csv")

# Print the first few rows
print(data.head())

print(f"The dataset has {data.shape[0]} rows and {data.shape[1]} columns.")
data.info()
data.describe()
data['1. What is your biggest reason for learning to code?'].value_counts()
print(data.isnull().sum())

print("Unique values in '1. What is your biggest reason for learning to code?'")
print(data['1. What is your biggest reason for learning to code?'].value_counts())
print("\nUnique values in '14. Which of these careers are you interested in?'")
print(data['14. Which of these careers are you interested in?'].value_counts())
print("\nUnique values in '20. Regarding employment status, are you currently....'")


numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
print(f"Numerical columns: {numerical_cols}")
corr = data[numerical_cols].corr()
print("\nCorrelation matrix:")
print(corr)

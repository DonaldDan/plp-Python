import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset from sklearn
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = data.target_names[data.target]

# Display the first few rows
print(df.head())

# Explore the structure of the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Basic statistics of numerical columns
print(df.describe())

# Group by species and compute the mean for numerical columns
grouped = df.groupby('species').mean()
print(grouped)

import matplotlib.pyplot as plt
import seaborn as sns

# Setting the style of the plots
sns.set(style="whitegrid")

# 1. Bar Chart: Average petal length by species
plt.figure(figsize=(8,6))
sns.barplot(x='species', y='petal length (cm)', data=df, estimator='mean')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 2. Histogram: Distribution of Sepal Length
plt.figure(figsize=(8,6))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 3. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8,6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', data=df, hue='species', palette='deep')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()



try:
    # Loading the data (if from a file)
    df = pd.read_csv("sklearn.datasets.csv")
except FileNotFoundError:
    print("The dataset file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Check for missing values and handle them
if df.isnull().sum().any():
    print("Missing values found!")
    df.fillna(df.mean(), inplace=True)  # Filling missing values with the column mean

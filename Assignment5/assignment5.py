import math
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

print("=== 1. MATH MODULE DEMONSTRATION ===")
x = 25.6
print(f"Number: {x}")
print(f"Ceil({x}): {math.ceil(x)}")
print(f"Floor({x}): {math.floor(x)}")
print(f"Fabs({-x}): {math.fabs(-x)}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Square root of 16: {math.sqrt(16)}\n")

print("=== 2. NUMPY & SCIPY DEMONSTRATION ===")
# Creating a sample NumPy array
arr = np.array([10, 20, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"NumPy Array: {arr}")
print(f"Mean: {np.mean(arr)}")
print(f"Median: {np.median(arr)}")
print(f"Standard Deviation: {np.std(arr):.2f}")

# SciPy statistical computation (Mode)
mode_result = stats.mode(arr, keepdims=True)
print(f"Mode using SciPy: {mode_result.mode[0]} (count: {mode_result.count[0]})\n")

print("=== 3. PANDAS DATA PREPROCESSING ===")
# Loading a built-in sample dataset (Iris) via URL or creating a dummy DataFrame if offline
# Using a reliable raw URL for Iris dataset
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
try:
    df = pd.read_csv(url)
    print("Dataset loaded successfully from web!")
except Exception as e:
    print("Network error, creating local fallback dataframe.")
    data = {
        'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0],
        'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6],
        'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4],
        'species': ['setosa', 'setosa', 'setosa', 'setosa', 'setosa']
    }
    df = pd.DataFrame(data)

# Display first few records
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check for null values
print("\nNull values in dataset:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

print("\n=== 4. MATPLOTLIB DATA VISUALIZATION ===")
print("Generating and saving plots...")

# 1. Line Chart / Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(df['sepal_length'], df['sepal_width'], color='purple', label='Sepal Data')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.close()

# 2. Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['sepal_length'], bins=10, color='teal', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('histogram.png')
plt.close()

print("Plots generated successfully and saved as PNG files!")
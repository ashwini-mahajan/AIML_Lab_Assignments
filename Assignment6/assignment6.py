import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
columns = [
    "age", "workclass", "fnlwgt", "education",
    "education_num", "marital_status", "occupation",
    "relationship", "race", "sex", "capital_gain",
    "capital_loss", "hours_per_week", "native_country",
    "income"
]

df = pd.read_csv(url, names=columns, skipinitialspace=True, na_values="?")

print("First five records:")
print(df.head())
print("\nDataset shape:", df.shape)

print("\nMissing values before processing:")
print(df.isnull().sum())

numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns
for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_cols = df.select_dtypes(include=["object", "category"]).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after processing:")
print(df.isnull().sum())

df_encoded = pd.get_dummies(df, columns=categorical_cols.drop("income").tolist(), dtype=int)
df_encoded["income"] = LabelEncoder().fit_transform(df_encoded["income"])

print("\nDataset after encoding:")
print(df_encoded.head())

numeric_features = ["age", "fnlwgt", "education_num", "capital_gain", "capital_loss", "hours_per_week"]
scaler = MinMaxScaler()
df_encoded[numeric_features] = scaler.fit_transform(df_encoded[numeric_features])

print("\nDataset after normalization:")
print(df_encoded.head())

df_encoded.to_csv("adult_income_processed.csv", index=False)
print("\nProcessed dataset saved successfully!")
print("Final dataset shape:", df_encoded.shape)

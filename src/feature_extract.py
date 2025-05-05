import os
import pandas as pd
from pathlib import Path


data = pd.read_csv("data/preprocessed/student_depression_dataset_processed.csv")
# Served its purpose in the reporting section, don't need for model training
if 'Total Pressure' in data.columns:
    data.drop(columns=['Total Pressure'], inplace=True)
# one-hot encoding for categoricals
cat_features = ['Gender', 'City', 'Profession', 'Degree', 
                'Have you ever had suicidal thoughts ?', 'Family History of Mental Illness', 'Financial Stress']
data_encoded = pd.get_dummies(data, columns=cat_features, drop_first=True)
drop_cols = ['id', 'Depression', 'Have you ever had suicidal thoughts ?', 
             'Family History of Mental Illness', 'Gender', 'City', 
             'Profession', 'Degree', 'Financial Stress']
data_encoded_clean = data_encoded.drop(columns=drop_cols)
print("Columns after encoding:", data_encoded.columns.tolist())

# Define keys for the original categorical columns that were encoded
cat_keys = ["Have you ever had suicidal thoughts ?", "Family History of Mental Illness", 
            "Gender", "City", "Profession", "Degree", "Financial Stress"]

# Identify dummy columns that contain any of these keys
dummy_cols = [col for col in data_encoded_clean.columns if any(key in col for key in cat_keys)]

# Build a list of columns to drop only if they exist in data_encoded
drop_cols = []
for col in ['id', 'Depression']:
    if col in data_encoded_clean.columns:
        drop_cols.append(col)
drop_cols += dummy_cols  # Add dummy columns to drop list

# Drop the columns
X = data_encoded_clean.drop(columns=drop_cols)

# Ensure target variable is correctly defined. If 'Depression' was dropped, use the original target.
if 'Depression' in data_encoded_clean.columns:
    y = data_encoded_clean['Depression']
    y.name = "target"
else:
    # If 'Depression' is not in data_encoded_clean, use it from the original data
    y = data['Depression']
    y.name = "target"

os.makedirs("data/model_ready", exist_ok=True)
model_ready = pd.concat([X, y], axis=1)
model_ready.to_csv("data/model_ready/student_depression_dataset_model_ready.csv", index=False)

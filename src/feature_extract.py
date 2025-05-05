import os
import pandas as pd
from pathlib import Path


data = pd.read_csv("data/preprocessed/student_depression_dataset_processed.csv")
# Served its purpose in the reporting section, don't need for model training
if 'Total Pressure' in data.columns:
    data.drop(columns=['Total Pressure'], inplace=True)

# one-hot encoding for categoricals
data_encoder.drop(columns=["id", "Depression"], inPlace=True)
cat_features = ['Gender', 'City', 'Profession', 'Degree', 
                'Have you ever had suicidal thoughts ?', 'Family History of Mental Illness', 'Financial Stress']
data_encoded = pd.get_dummies(data_encoder, columns=cat_features, drop_first=True)
print("Columns after encoding:", data_encoded.columns.tolist())

y = data['Depression']
y.name = 'target'
X = data_encoded

os.makedirs("data/model_ready", exist_ok=True)
model_ready = pd.concat([X, y], axis=1)
model_ready.to_csv("data/model_ready/student_depression_dataset_model_ready.csv", index=False)

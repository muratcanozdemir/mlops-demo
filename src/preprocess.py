import os
import pandas as pd
import re
import numpy as np

def extract_hours(s):
    # Find a number (including decimals)
    match = re.search(r"(\d+(\.\d+)?)", str(s))
    return float(match.group(1)) if match else np.nan


data = pd.read_csv("data/raw/student_depression_dataset.csv")
data['Depression'] = data['Depression'].astype(int)

cat_cols = ['Gender', 'City', 'Profession', 'Degree',
            'Have you ever had suicidal thoughts ?', 
            'Family History of Mental Illness']
for col in cat_cols:
    data[col] = data[col].astype('category')

data['Sleep Duration'] = data['Sleep Duration'].apply(extract_hours)
data['Financial Stress'] = data['Financial Stress'].astype('category')

for col in ['Sleep Duration']:
    if data[col].isnull().sum() > 0:
        data[col].fillna(data[col].median(), inplace=True)

data['Total Pressure'] = data['Academic Pressure'] + data['Work Pressure']

os.makedirs("data/preprocessed", exist_ok=True)
df.to_csv("data/preprocessed/student_depression_dataset_processed.csv", index=False)
    

import pandas as pd
# Standardize numerical features
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.model_selection import train_test_split

import json
import joblib
import os
import sys

# Ensure outputs directory exists
output_dir = os.path.join(sys.argv[2], "outputs")
os.makedirs(output_dir, exist_ok=True)

input_path = sys.argv[1]
data = pd.read_csv(input_path)
X = df.drop(columns=["target"])
y = df["target"]

scaler = StandardScaler()
num_feats = ['Age', 'Academic Pressure', 'Work Pressure', 'CGPA', 
             'Study Satisfaction', 'Job Satisfaction', 'Sleep Duration', 
             'Work/Study Hours', 'Total Pressure']
X[num_feats] = scaler.fit_transform(X[num_feats])

print("Feature matrix shape:", X.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

# Predictions and evaluation
y_pred_log = log_model.predict(X_test)
print("Logistic Regression Classification Report:")
print(classification_report(y_test, y_pred_log))
# Generate report as a dict
report_dict = classification_report(y_test, y_pred_log, output_dict=True)
cm_log = confusion_matrix(y_test, y_pred_log)
report_dict["confusion_matrix"] = cm_log

y_prob_log = log_model.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob_log)
roc_auc_log = auc(fpr, tpr)
report_dict["fpr"] = fpr
report_dict["tpr"] = tpr
report_dict["thresholds"] = thresholds
report_dict["roc_auc_log"] = roc_auc_log

with open(f"{output_dir}/metrics.json", "w") as f:
    json.dump(report_dict, f, indent=4)

# Save predictions
pd.DataFrame({
    "y_true": y_test,
    "y_pred": y_pred_log,
    "y_prob": y_prob_log
}).to_csv("f{output_dir}/predictions.csv", index=False)

# Save model + scaler
joblib.dump({
    "model": log_model,
    "scaler": scaler
}, f"{output_dir}/model.pkl")

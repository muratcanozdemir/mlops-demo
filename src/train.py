import pandas as pd
# Standardize numerical features
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import json
import joblib


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

with open("outputs/metrics.json", "w") as f:
    json.dump(report_dict, f, indent=4)
joblib.dump(log_model, "outputs/model.pkl")
with open("outputs/predictions.csv", "w") as f:
    json.dump(y_pred_log)
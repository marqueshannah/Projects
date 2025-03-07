import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset from file
df = pd.read_csv("project1.txt")

# Data Cleaning
# Replace '?' and '*' with NaN
df.replace({'?': np.nan, '*': np.nan}, inplace=True)

# Convert categorical variables into numeric form
df_encoded = pd.get_dummies(df, columns=['age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'breast', 'breast-quad', 'irradiat'], drop_first=True)

# Encode the target variable
df_encoded['class'] = df['class'].map({'no-recurrence-events': 0, 'recurrence-events': 1})

# Splitting the dataset
X = df_encoded.drop(columns=['class'])
y = df_encoded['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN Classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# KNN with GridSearchCV
param_grid = {'n_neighbors': [1, 3, 5, 7, 9]}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
y_pred_knn_cv = grid_search.predict(X_test)

# Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred_log_reg = log_reg.predict(X_test)

# Evaluation
print("KNN Classifier:")
print(classification_report(y_test, y_pred_knn))
print("KNN with GridSearchCV:")
print(classification_report(y_test, y_pred_knn_cv))
print("Logistic Regression:")
print(classification_report(y_test, y_pred_log_reg))

# Visualizing class distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='class')
plt.title("Class Distribution")
plt.xticks(rotation=45)
plt.show()

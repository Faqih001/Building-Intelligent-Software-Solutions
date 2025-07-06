# Task 3: Predictive Analytics for Resource Allocation
# Using the Kaggle Breast Cancer Dataset to predict issue priority (high/medium/low)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

def main():
    # Load dataset (ensure the CSV is in the same directory or provide the correct path)
    df = pd.read_csv('breast_cancer_data.csv')

    # Example preprocessing (customize as needed)
    df = df.dropna()
    df['priority'] = df['diagnosis'].map({'M': 'high', 'B': 'low'})  # Example mapping

    X = df.drop(['priority', 'diagnosis'], axis=1)
    y = df['priority']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate model
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    print("Accuracy:", accuracy)
    print("F1 Score:", f1)

if __name__ == "__main__":
    main()

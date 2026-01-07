import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load Kaggle dataset

data = pd.read_csv("dataset/heart.csv")



# Features and target
X = data.drop("condition", axis=1)  # all features
y = data["condition"]               # target variable



# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
model.fit(X_train, y_train)

# Save model and scaler
with open("models/heart_model.pkl", "wb") as f:
    pickle.dump((model, scaler, X.columns.tolist()), f)

print("✅ Model trained using Kaggle Heart Disease UCI dataset")

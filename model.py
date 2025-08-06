# train_model.py
import pickle
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load California housing dataset
data = fetch_california_housing(as_frame=True)
df = data.frame.copy()

target = "MedHouseVal"

# Select top 4 correlated numeric features
numeric_cols = df.drop(columns=[target]).select_dtypes(include=["number"]).columns
corrs = df[numeric_cols].corrwith(df[target]).abs().sort_values(ascending=False)
features = corrs.head(4).index.tolist()

# Prepare data
X = df[features].values
y = df[target].values

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Ridge regression
model = Ridge(alpha=1.0, random_state=42)
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))


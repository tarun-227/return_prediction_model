import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('product_data.csv')

# Encode 'Category' using LabelEncoder
le = LabelEncoder()
df['Category'] = le.fit_transform(df['Category'])

# Feature set and target
X = df[['Category', 'Price', 'Num_Orders', 'Past_Returns']]
y = df['Return_Percentage']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model and encoder
joblib.dump(model, 'model.pkl')
joblib.dump(le, 'encoder.pkl')
print("✅ Model and encoder saved.")

# Plot feature importance
importances = model.feature_importances_
features = X.columns

plt.barh(features, importances)
plt.xlabel("Feature Importance")
plt.title("Feature Impact on Return Prediction")
plt.tight_layout()
plt.savefig("feature_importance.png")
print("📊 Feature importance chart saved as 'feature_importance.png'")

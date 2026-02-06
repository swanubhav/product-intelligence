import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("data/processed/slow_death_features.csv")

df["dying"] = (df["sales_count"] < df["sales_count"].median()).astype(int)

X = df[["price", "rating_avg", "sales_count", "return_rate", "product_age_days"]]
y = df["dying"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "src/models/slow_death_model.pkl")

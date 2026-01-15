import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

df = pd.DataFrame({"x":[1,2,3,4,5], "y":[2,4,6,8,10]})
X = df[["x"]]
y = df["y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

with mlflow.start_run():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    mlflow.log_param("model", "LinearRegression")
    mlflow.log_metric("mse", mse)

    joblib.dump(model, "model.pkl")
    mlflow.log_artifact("model.pkl")

    print("Model trained. MSE:", mse)

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# dataset
data = {
    "experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
}

df = pd.DataFrame(data)

X = df[["experience"]]
y = df["salary"]

# model
model = LinearRegression()
model.fit(X, y)

# save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Linear Regression model trained & saved!")
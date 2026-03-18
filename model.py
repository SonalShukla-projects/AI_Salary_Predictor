import pickle
from predictor import predict

with open("model.pkl", "wb") as f:
    pickle.dump(predict, f)

print("✅ model.pkl created successfully")
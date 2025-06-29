from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model and encoder
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

app = FastAPI()

# Input data format
class ProductInput(BaseModel):
    Category: str
    Price: float
    Num_Orders: int
    Past_Returns: int

# API endpoint
@app.post("/predict")
def predict_return(input: ProductInput):
    # Encode category
    cat_encoded = encoder.transform([input.Category])[0]
    
    # Prepare feature vector
    features = np.array([[cat_encoded, input.Price, input.Num_Orders, input.Past_Returns]])
    
    # Predict
    pred = model.predict(features)[0]
    
    return {"Predicted Return Percentage": round(pred, 2)}

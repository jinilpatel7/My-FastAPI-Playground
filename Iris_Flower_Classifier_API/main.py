from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("Iris_Flower_Classifier_API/iris_model.pkl")

app = FastAPI(title="Iris Flower Classifier")

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Prediction 
@app.post("/predict")
def predict_species(features: IrisFeatures):
    data = np.array([[features.sepal_length, 
                      features.sepal_width, 
                      features.petal_length, 
                      features.petal_width]])
    prediction = model.predict(data)[0]
    species = ["setosa", "versicolor", "virginica"][prediction]
    return {"predicted_species": species}


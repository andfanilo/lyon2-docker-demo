import joblib
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()
target_names = ['setosa', 'versicolor', 'virginica']
model = joblib.load("../training/model.joblib")

@app.get("/")
def status():
    return {"Hello": "World"}


@app.post("/predict")
def predict(item: Item):
    item_data = jsonable_encoder(item)
    prediction = model.predict([(list(item_data.values()))]).item()
    prediction = target_names[prediction]
    return {
        "prediction": prediction
    }

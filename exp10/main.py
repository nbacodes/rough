from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict")
def predict(inp: Input):
    # simple logic like manual example
    return {"prediction": inp.feature1 + inp.feature2}

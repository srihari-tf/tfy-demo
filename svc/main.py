import os
from typing import List

import mlfoundry
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI(docs_url="/")
model = mlfoundry.get_client().get_model(os.getenv("MODEL_VERSION_FQN")).load()
CLASS_NAMES = ['setosa', 'versicolor', 'virginica']

class Instance(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class Request(BaseModel):
    instances: List[Instance]


def postprocess(prediction):
    return dict(zip(CLASS_NAMES, prediction.tolist()))

@app.post("/predict")
def predict(request: Request):
    df = pd.DataFrame(request.dict()["instances"])
    predictions = [postprocess(p) for p in model.predict_proba(df)]
    return {"predictions": predictions}
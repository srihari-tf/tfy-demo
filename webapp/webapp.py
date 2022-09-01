import os

import mlfoundry
import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris

@st.cache()
def load_model():
    RUN_FQN = os.getenv("MLF_RUN_FQN")
    run = mlfoundry.get_client().get_run(RUN_FQN)
    return run.get_model()

@st.cache()
def load_dataset():
    return load_iris()


model = load_model()
target_names =  load_dataset().target_names

def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    data = dict(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width,
    )
    return target_names[int(model.predict(pd.DataFrame([data]))[0])]

st.title('Identify the Iris plant')

sl = st.number_input("Sepal length (cm)")
sw = st.number_input("Sepal width (cm)")
pl = st.number_input("Petal length (cm)")
pw = st.number_input("Petal width (cm)")

st.text_area(label ="Prediction", value=predict(sl, sw, pl, pw), height =50)




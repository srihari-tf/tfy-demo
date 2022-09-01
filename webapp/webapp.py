import os

import mlfoundry
import pandas as pd
import strealmit as st

@st.cache()
def load_model():
    RUN_FQN = os.getenv("MLF_RUN_FQN")
    run = mlfoundry.get_client().get_run(RUN_FQN)
    return run.get_model()


model = load_model()

def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    data = dict(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width,
    )
    return int(model.predict(pd.DataFrame([data]))[0])

sl = st.number_input("Sepal length (cm)")
sw = st.number_input("Sepal width (cm)")
pl = st.number_input("Petal length (cm)")
pw = st.number_input("Petal width (cm)")

st.write(predict(sl, sw, pl, pw))


# Starting the application

`uvicorn main:app --port 8080 --host 0.0.0.0`

Envs:

* `TFY_HOST = https://app.develop.truefoundry.tech` 
* `TFY_API_KEY = tfy-secret://srihari:my-secret:TFY_API_KEY`
* `MODEL_VERSION_FQN = model:truefoundry/user-truefoundry/demo-12-10-22/iris-classifier:2`
# Replace `YOUR_SECRET_FQN`, `YOUR_WORKSPACE_FQN`
# with the actual values.
import logging

from servicefoundry import Build, Service, PythonBuild

logging.basicConfig(level=logging.INFO)

image = Build(
    build_spec=PythonBuild(
        command="uvicorn inference_api:app --port 8000 --host 0.0.0.0",
        requirements_path="inference_requirements.txt",
    ),
)
env = [
    {
        "name": "MLF_API_KEY",
        "value": "tfy-secret://user-truefoundry:my-secret-group:MLF_API_KEY",
    },
    {
        "name": "MLF_RUN_FQN",
        "value": "truefoundry/user-truefoundry/iris-classification/delectable-caterpillar",
    },
]
service = Service(
    name="inference-svc",
    image=image,
    ports=[{"port": 8000}],
    env=env,
)

deployment = service.deploy(workspace_fqn="v1:local:demo-workspace")
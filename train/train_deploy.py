import logging

from servicefoundry import (
    Build,
    Job,
    PythonBuild,
    ManualTrigger
)

logging.basicConfig(level=logging.INFO)

image = Build(
    build_spec=PythonBuild(
        command="python train.py",
        requirements_path="train_requirements.txt",
    )
)

env = [
    {
        "name": "MLF_API_KEY",
        "value": "tfy-secret://user-truefoundry:my-secret-group:MLF_API_KEY",
    }
]

job = Job(
    name="training-job",
    image=image,
    env=env,
    trigger=ManualTrigger(run=True)
)

job.deploy(workspace_fqn="v1:local:demo-workspace")

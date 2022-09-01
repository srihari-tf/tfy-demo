# Replace `YOUR_SECRET_FQN`, `YOUR_WORKSPACE_FQN`
# with the actual values.
import logging

from servicefoundry import (
    Build,
    Job,
    PythonBuild,
    ManualTrigger
)

logging.basicConfig(level=logging.INFO)

# NOTE: Here we are defining the image build specification.
# servicefoundry uses this specification to automatically create
# a Dockerfile and build an image,
image = Build(
    build_spec=PythonBuild(
        command="python train.py",
        requirements_path="train_requirements.txt",
    )
)
env = [
    {
        "name": "MLF_API_KEY",
        # NOTE:- We will automatically map the secret value to the environment variable.
        "value": "tfy-secret://user-truefoundry:my-secret-group:MLF_API_KEY",
    }
]

job = Job(
    name="training-job",
    image=image,
    env=env,
    trigger=ManualTrigger(type="manual", run=True)
)

job.deploy(workspace_fqn="v1:local:qaifi-workspace")

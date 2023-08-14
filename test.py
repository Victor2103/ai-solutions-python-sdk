import os

from dotenv import load_dotenv

from ov_hcloud_ai_solution_client import AuthenticatedClient
from ov_hcloud_ai_solution_client.api.job import job_new
from ov_hcloud_ai_solution_client.models import Job, JobSpec
from ov_hcloud_ai_solution_client.types import Response

load_dotenv()
TOKEN = os.getenv("TOKEN")

request = {
    "command": ["sleep", "60"],
    "deletionRequested": False,
    "image": "bash",
    "resources": {"cpu": 1, "gpu": 0},
    "timeout": 4,
}


client = AuthenticatedClient(
    base_url="https://gra.training.ai.cloud.ovh.net", token=TOKEN
)
with client as client:
    response: Response[Job] = job_new.sync_detailed(
        client=client, json_body=JobSpec.from_dict(request)
    )

print(response.content)

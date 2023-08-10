import os

from dotenv import load_dotenv
from prefect_ovh.flows import create_job_and_wait_until_is_done

# Load environments variables
load_dotenv()

TOKEN = os.getenv("TOKEN")

flow = create_job_and_wait_until_is_done(
    token=TOKEN, image="bash", command=["sleep", "120"]
)
print("Here is your job : ", flow)

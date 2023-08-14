import os

from dotenv import load_dotenv
from prefect_ovh.flows import create_job_and_wait_until_is_done

# Load environments variables
load_dotenv()

TOKEN = os.getenv("TOKEN")

flow = create_job_and_wait_until_is_done(
    token=TOKEN,
    image="bash",
    command=["sleep", "120"],
    telegram=False,
    api_telegram=os.getenv("API_TELEGRAM"),
    chat_id=os.getenv("CHAT_ID"),
)
print("Here is your job : ", flow)

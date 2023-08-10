import os

from dotenv import load_dotenv
from prefect.blocks.notifications import AppriseNotificationBlock

# Load environments variables
load_dotenv()

telegram_webhook_block = AppriseNotificationBlock(
    url=f"tgram://{os.getenv('API_TELEGRAM')}/{os.getenv('CHAT_ID')}/"
)

telegram_webhook_block.notify("Hello from Prefect!")

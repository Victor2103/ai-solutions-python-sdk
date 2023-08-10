from prefect.blocks.notifications import TelegramWebhook
from pydantic import SecretStr

telegram_webhook_block = TelegramWebhook(
    bot_token=SecretStr("0123456789:qwertyuiopasdfghjklzxcvbnm"), chat_id="123456789"
)
telegram_webhook_block.notify("Hello from Prefect!")

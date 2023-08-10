from ov_hcloud_ai_solution_client import AuthenticatedClient
from ov_hcloud_ai_solution_client.models import Me
from ov_hcloud_ai_solution_client.api.me import me

client = AuthenticatedClient(base_url="https://gra.training.ai.cloud.ovh.net",
                             token='SAnNu2i6R+K6JOYaAUDclnTWx1XH3Ck7+hIfr2dWj4oLEbt+XvhMnvUUegm0QFY9')
with client as client:
    response: Me = me.sync_detailed(client=client)

print(response)

client = AuthenticatedClient(base_url="https://gra.training.ai.cloud.ovh.net",
                             token='SAnNu2i6R+K6JOY7+hIfr2dWj4oLEbt+XvhMnvUUegm0QFY9')

with client as client:
    response: Me = me.sync_detailed(client=client)

print(response)

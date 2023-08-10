from ov_hcloud_ai_solution_client import AuthenticatedClient
from ov_hcloud_ai_solution_client.models import JobSpec, Job
from ov_hcloud_ai_solution_client.api.job import job_new, job_get, job_log, job_start,job_kill, job_delete
from ov_hcloud_ai_solution_client.types import Response




def create_request(image,http_port=8080,command=[],listEnvVars=[],dicLabels={},name=None,cpu=0,gpu=1,sshPublicKeys=[],volumes=[]):
    request={
  "command": command,
  "defaultHttpPort": http_port,
  "deletionRequested": False,
  "envVars": listEnvVars,
  "labels": dicLabels,
  "image": image,
  "name": name,
  "resources": {
    "cpu": cpu,
    "gpu": gpu
  },
  "sshPublicKeys": sshPublicKeys,
  "volumes": volumes
}
    if name==None:
        name=request.pop("name")
    if cpu!=0:
        request.update({"resources":{
            "cpu": cpu,
            "gpu": 0
            }
                        })
    print(request)
    return(request)

#print(create_job({"image":"ubuntu"},{"cpu":7},{"env":["name","value"]},{"env":["name2","value2"]},{"labels":{"reader":"ai-apps"}}))
#with open("test.json","w") as f:
#    f.write(response.content.decode())

"""
client=AuthenticatedClient(base_url="https://gra.training.ai.cloud.ovh.net",token='SAnNu2i6R+K6JOYaAUDclnTWx1XH3Ck7+hIfr2dWj4oLEbt+XvhMnvUUegm0QFY9')
with client as client:
    response: Response[Job] = job_new.sync_detailed(client=client,json_body=JobSpec.from_dict(create_request(image="python",cpu=7,http_port=7000)))
    #response: Response[Job] = job_new.sync_detailed(client=client,json_body=JobSpec.from_dict({"image":"ubuntu"}))
print(response.content.decode())
"""

"""
Example of a volume : 
    {
      "cache": False,
      "dataStore": {
        "alias": "GRA",
        "archive": "archive.tar",
        "container": "container",
        "prefix": "string"
      },
      "mountPath": "/workspace/test",
      "permission": "RO",
      "privateSwift": {
        "archive": "archive.tar",
        "container": "container",
        "prefix": "string",
        "region": "GRA"
      },
    }
"""

client=AuthenticatedClient(base_url="https://gra.training.ai.cloud.ovh.net",token='SAnNu2i6R+K6JOYaAUDclnTWx1XH3Ck7+hIfr2dWj4oLEbt+XvhMnvUUegm0QFY9')
with client as client:
    response: Response[Job] = job_delete.sync_detailed(id="2fcbbb1b-8d03-4a31-b5dd-97a76b00a44a",client=client)

print(client)

print(response.content.decode())

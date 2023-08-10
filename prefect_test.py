from prefect_ovh.flows import test_client, test_infos, test_logs, test_start_job, test_stop_job, test_delete_job
import json

TOKEN="SAnNu2i6R+K6JOYaAUDclnTWx1XH3Ck7+hIfr2dWj4oLEbt+XvhMnvUUegm0QFY9"
      
#result=json.loads(test(token=TOKEN))

#print("Welcome",test(token=TOKEN))

#print("Welcome",test_client(token=TOKEN))

#print("Here is your job : ",test_infos(token=TOKEN,id_job="358b2544-51cd-41d5-add8-1eaba8337acb"))

#print("Here are the logs of your job : ",test_logs(token=TOKEN,id_job="358b2544-51cd-41d5-add8-1eaba8337acb"))

print(test_delete_job(token=TOKEN,id_job="2ee0322c-dbfb-4b15-8527-f273ac3b0943"))
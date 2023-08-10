from prefect_ovh.flows import create_job_and_wait_until_is_done

TOKEN = "SAnNu2i6R+K6JOYaAUDclnTWx1XH3Ck7+hIfr2dWj4oLEbt+XvhMnvUUegm0QFY9"

print("Here is your job : ",
      create_job_and_wait_until_is_done(token=TOKEN,
                                        image="bash",
                                        command=["sleep", "120"],
                                        timeout=30))

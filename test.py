import subprocess
import os

files = os.listdir("Job Descriptions")
redo = open("redo_job_descriptions.txt", "a")
for i in range(len(files)-1):
    f1, f2 = "Job Descriptions/" + files[i], "Job Descriptions/" + files[i+1]
    if int(subprocess.check_output(f"cmp --silent '{f1}' '{f2}' && echo '1' || echo '0'",
                text=True,
                stderr=subprocess.STDOUT,
                shell=True).strip()) == 1:
        redo.write(f"{files[i].split('.')[0]}\n")
        redo.write(f"{files[i+1].split('.')[0]}\n")
redo.close()

import requests
from bs4 import BeautifulSoup
import sys
import time
import glob

def get_job_description(job_id):
    target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
    resp = requests.get(target_url.format(job_id))
    if resp.status_code == 429:
        t = 4
        while resp.status_code == 429:
            print(f"errored out, sleeping for {t}")
            time.sleep(t)
            t *= 2
            resp = requests.get(target_url.format(job_id))

    soup=BeautifulSoup(resp.text,features='html.parser')
    s = soup.find(class_="description")
    return str(s)

with open('job_ids') as f:
    job_ids = f.readlines()

    job_ids = [id.strip() for id in job_ids]

    for i in range(len(job_ids)):
        id = job_ids[i]
        try:
            print(id)
            desc = get_job_description(id)
        except Exception as e:
            print(f'failed at line {i}, {id}: \n{e}')
        with open(f'Job Descriptions/{id}.txt','w') as f:
            f.write(desc)

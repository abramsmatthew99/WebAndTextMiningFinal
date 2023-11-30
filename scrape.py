import requests
from bs4 import BeautifulSoup
import sys
import time

def get_job_description(job_id):
    target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
    #print(target_url.format(job_id))
    resp = requests.get(target_url.format(job_id))
    if resp.status_code == 429:
        t = 4
        while resp.status_code == 429:
            time.sleep(t)
            t *= 2
            resp = requests.get(target_url.format(job_id))

    soup=BeautifulSoup(resp.text,features='html.parser')
    return soup.get_text().strip()


with open('xaa') as f:
    job_ids = f.readlines()

job_ids = [id.strip() for id in job_ids]

for id in job_ids:
    desc = get_job_description(id)
    print(id)
    with open(f'Job Descriptions/{id}.txt','w') as f:
        f.write(desc)

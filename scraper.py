import requests
from bs4 import BeautifulSoup
import math
import time


def get_job_ids(start_page, end_page):
    target_url = 'https://www.linkedin.com/jobs' + \
        '/search/?currentJobId=3759540843&keywords' + \
        '=computer%20science&origin=JOBS_HOME_SEARCH_BUTTON' + \
        '&refresh=true&start=25'
    #Results are loaded on an infinite scroll basis, but the search URL provides a workaround using the start keyword
    '''
    jobs = []

    for i in range(start_page,end_page):

        print(f'Page {i}')
        #Change the start index for the search
        res = requests.get(target_url.format(i))
        if res.status_code == 429:
            t = 4
            while res.status_code == 429:
                t *= 2
                time.sleep(t)
                res = requests.get(target_url.format(i))
        soup = BeautifulSoup(res.text, features='html.parser')
        jobs_list = soup.find_all("li")
        for job in jobs_list:
            valid_job = job.find('div', {'class': 'base-card'})
            if valid_job:
                #This is just the structure of how to find the Job ID
                jobs.append(valid_job.get('data-entity-urn').split(":")[3])
    return jobs
    '''
    print(target_url)

get_job_ids(1,2)

#def get_job_description(job_id):
#    target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
#    resp = requests.get(target_url.format(job_id))
#    soup=BeautifulSoup(resp.text,features='html.parser')
#    return soup.get_text().strip()

#with open('job_ids.txt', 'r') as f:
#    for line in f:
#        with open(f'Job Descriptions\\{line.strip()}.txt', 'w+', encoding="utf-8") as out:
#            out.write(get_job_description(line.strip()))

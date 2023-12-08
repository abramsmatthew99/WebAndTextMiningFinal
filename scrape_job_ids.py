import requests
from bs4 import BeautifulSoup
import time

START = 0
END = 1000
n = 0
job_ids = open("job_ids.txt", "a")
target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=computer%20science&position={}&pageNum={}&start={}'
for i in range(6, 11):
    for j in range(11):
        for k in range(START, END, 25):
            try:
                url = target_url.format(i,j,k)
                res = requests.get(url)
                if res.status_code == 429:
                    t = 4
                    while res.status_code == 429:
                        print(f"errored out: sleeping for {t}")
                        time.sleep(t)
                        t *= 2
                        res = requests.get(url)
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.find_all(class_='base-card__full-link')
                for item in items:
                    n += 1
                    job_id = item.get('href').split('?')[0].split('-')[-1]
                    job_ids.write(job_id)
                    job_ids.write('\n')
                    print(n, job_id)
                print(f"Success: position {i}, page {j}, batch {k}")
            except Exception as e:
                print(f"Failed at position {i}, page {j}, batch {k}: {e}")
job_ids.close()

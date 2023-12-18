from bs4 import BeautifulSoup
import requests

def scrape_cs_jargon():
    response = requests.get("https://www.coursereport.com/blog/coding-jargon-glossary-of-key-terms-at-coding-bootcamp")
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')
    output = set()

    for row in rows:
        cell = row.find('td')
        # print(cell)
        if cell:
            term = cell.find('strong')
            if term:
                output.add(term.get_text())
    response.close()
    return output

def scrape_wikipedia_glossary():
    output = set()
    response = requests.get("https://en.wikipedia.org/wiki/Glossary_of_computer_science")
    soup = BeautifulSoup(response.content, 'html.parser')
    terms = soup.findAll('dfn', {'class': 'glossary'})
    for term in terms:
        output.add(term.get_text())
    response.close()
    return output

def scrape_wikipedia_languages():
    output = set()
    response = requests.get("https://en.wikipedia.org/wiki/List_of_programming_languages")
    soup = BeautifulSoup(response.content, 'html.parser')
    cols = soup.findAll('div', {'class': 'div-col'})
    for col in cols:
        list = col.find('ul')
        if list:
            terms = list.find_all()
            for term in terms:
                output.add(term.get_text())
    response.close()
    return output

def scrape_wikipedia_frameworks():
    output = set()
    response = requests.get("https://en.wikipedia.org/wiki/Category:Web_frameworks")
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.findAll('div', {'class':'mw-category-group'})
    for div in divs:
        u = div.find('ul')
        if u:
            l = u.findAll('li')
            for item in l:
                output.add(item.find('a').get_text().split()[0])
    response.close()
    return output

academia_terms = [
    'Bachelors',
    'Masters',
    'Doctorate',
    'Ph.D',
    'Phd'
    'Associate',
    'Certificate Programs',
    'Professional Degree',
    'Computer Science',
    'Biology',
    'Psychology',
    'Sociology',
    'Economics',
    'Political Science',
    'English Literature',
    'Mathematics',
    'Physics',
    'Chemistry',
    'History',
    'Environmental Science',
    'Business Administration',
    'Nursing',
    'Education',
    'Electrical Engineering',
    'Mechanical Engineering',
    'Civil Engineering',
    'Linguistics',
    'Philosophy',
    'Cybersecurity',
    'Data Science',
    'Artificial Intelligence',
    'Biomedical Engineering',
    'Graphic Design',
    'Film Studies',
    'International Relations',
    'Public Health',
    'Finance',
    'Marketing',
    'Journalism',
    'Astrophysics',
    'Geology',
    'Archaeology',
    'Forensic Science',
    'Social Work',
    'Fashion Design',
    'Game Development',
    'Aerospace Engineering',
    'Actuarial Science'
]

terms = set()
terms = terms.union(scrape_cs_jargon())
terms = terms.union(scrape_wikipedia_glossary())
terms = terms.union(scrape_wikipedia_languages())
terms = terms.union(scrape_wikipedia_frameworks())
terms = terms.union(set(academia_terms))

# write to file
with open('keywords_large_set.txt', 'w') as file:
    for term in terms:
        file.write(term + '\n')

   

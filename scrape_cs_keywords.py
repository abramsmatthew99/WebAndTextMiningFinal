from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.coursereport.com/blog/coding-jargon-glossary-of-key-terms-at-coding-bootcamp")
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all('tr')
terms = []

with open('keywords.txt', 'w') as file:
    for row in rows:
        cell = row.find('td')
        # print(cell)
        if cell:
            term = cell.find('strong')
            if term:
                file.write(term.get_text() + '\n')


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

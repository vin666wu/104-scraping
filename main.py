###104 crawler###
import requests
import time
from bs4 import BeautifulSoup
url_python = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
url_C_plus_plus = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=C%2B%2B&txtLocation='
print("please enter the skill that you are not familiar with")
unfamiliar_skill = input(" >")
print(f"filtering out {unfamiliar_skill}")

def find_jobs():
  html_text = requests.get(url_mysql).text
  soup = BeautifulSoup(html_text, 'html.parser')
  jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
  for index, job in enumerate(jobs):
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
      company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
      skills = job.find('span', class_='srp-skills').text.replace(' ','')
      more_info = job.header.h2.a['href']
      if unfamiliar_skill not in skills:
        with open(f'{index}.txt', 'w') as f:
          f.write(f"company name: {company_name.strip()} \n")
          f.write(f"required skills: {skills.strip()} \n")
          f.write(f"more info: {more_info} \n")
        print(f"file saved: {index}")
if __name__ == '__main__':
  while True:
    find_jobs()
    time_wait = 12*60
    print(f'waiting {time_wait} mins...')
    time.sleep(time_wait * 60)

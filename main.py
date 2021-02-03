from bs4 import BeautifulSoup
import requests
import time

print('Enter the search word')
search_word = input('>')

def find_jobs(search_word):
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={search_word}&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').find('span').text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            with open(f'post/{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name.strip()}\n')
                f.write(f'Required Skills: {skills.strip()}\n')
                f.write(f'Published Date: {published_date.strip()}\n')
                f.write(f'More Info: {more_info}')
            print(f'File saved: {index}.txt')

if __name__ == '__main__':
    while True:
        find_jobs(search_word)
        print('Waiting 10 seconds ...')
        time.sleep(10)
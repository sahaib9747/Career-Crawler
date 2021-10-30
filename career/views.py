from bs4 import BeautifulSoup
import requests

# from django.shortcuts import render
# from django.http import HttpResponse

def check(url, rurl):
    if 'https' in rurl:
        return rurl
    else:
        lst = url.split('career')[0]
        return lst + rurl

# Create your views here.
def bdtask():
    print("-----Company: BDTASK----")
    web = requests.get("https://www.bdtask.com/career.php")
    jobs = BeautifulSoup(web.text, 'lxml')
    jobs = jobs.find_all('div', class_ = 'job_post')  # select all the div named job_post
    for job in jobs:  # iterate div object
        title = job.find('h3').text  
        if 'python' in title.lower():
            exp_deadline = job.find('div', class_ = 'job_exp').find_all('p')
            exp = exp_deadline[0].text.split(':')[1]
            deadline = exp_deadline[1].text.split(':')[1]
            details = job.find('div', class_ = 'job_details').a['href']
            details = check(web.url, details)

            print(f"\nJob Title: {title}\nJob Exp: {exp}\nDeadline: {deadline}\nDetails: {details}")


def cefalo():
    print("-----Company: CEFALO----")
    web = requests.get('https://www.cefalo.com/en/career').text
    jobs = BeautifulSoup(web, 'lxml')

    jobs = jobs.find_all('div', class_ ="custom-column-wrap-inner")

    for job in jobs:
        title = job.find('h3').text
        short_sum = job.find('p').text
        details = job.find('a', class_='more-button')['href']

        req = BeautifulSoup(requests.get(details).text, 'lxml')
        req = req.find('span', id='hs_cos_wrapper_widget_6377555919_').find_all('ul')[-1].find('span').text

        print(f"\nJob Title: {title}\nShort Summary: {short_sum}\nDeadline: {req}\nDetails: {details}")

bdtask()
cefalo()

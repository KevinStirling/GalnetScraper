#!/usr/bin/env python
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


base_url = 'https://community.elitedangerous.com/en/galnet/'
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT",
          "NOV", "DEC"]
years = ["3301", "3302", "3303", "3304", "3305"]
f = open('galnet.json', 'a')


def main():
    with open('galnet.json', 'a') as f:
        f.write('{"set": [')
    for y in years:
        for m in months:
            for d in range(32):
                if d < 10:
                    scrape(base_url+"0"+str(d)+"-"+m+"-"+y)
                    print(base_url+str(d)+"-"+m+"-"+y)
                else:
                    scrape(base_url+str(d)+"-"+m+"-"+y)
                    print(base_url+str(d)+"-"+m+"-"+y)
    f.write(']}')
    f.close()


def scrape(url):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    for p in html.find_all('div', 'article'):
        print(p.text)
        with open('galnet.json', 'a') as f:
            corrected = p.text.replace('"', '\'').lstrip()
            f.write('{"Article": "'+corrected+'",')
        for p in p.find_all('div', 'i_right'):
            with open('galnet.json', 'a') as f:
                f.write('"Date": "'+p.text+'"},')


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                print(resp.content)
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)
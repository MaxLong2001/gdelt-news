import json
import os
import requests
from datetime import date
from bs4 import BeautifulSoup

def get_headline_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            headline = soup.find('h1').get_text()
            return headline
        else:
            print(f"Failed to fetch the webpage. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

folder = '/Users/longyizhou/Projects/gdelt-news-headlines/v2/'
filelist = sorted(os.listdir(folder))

last_url = None
for fzip in filelist:
    cur_date = date(int(fzip[0:4]), int(fzip[4:6]), int(fzip[6:8]))
    with open(folder + fzip, 'r') as f:
        lines = f.readlines()
        for l in lines:
            url = l.strip().split('\t')[-1]
            if last_url == url:
                last_url = url
                continue
            last_url = url
            
            print(f"Fetching {url}")
            headline = get_headline_from_url(url)
            if headline is None:
                continue
            headline = headline.strip()
            print(f"\tGot {headline}")
            data = {
                "article_date": fzip[0:8],
                "url": url,
                "title": headline
            }
            json.dumps(data)
            with open('gdelt_data_20220101.jsonl', 'a') as fjson:
                fjson.write(json.dumps(data) + '\n')


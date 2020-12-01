import os
from selenium import webdriver
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import argparse

def scrape_criterion():
    options = Options()
    options.headless = True
    driver_path = '/Users/Suryadip/chromedriver'
    lists_home_url = 'https://www.criterion.com/current/category/8-top-10-lists'
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get(lists_home_url)

    # press the load more button 9 times (there are 10 pages)
    for i in range(9):
        load_more = driver.find_elements_by_class_name("linkbut_plain")
        lists = driver.find_elements_by_class_name('more-article')
        print('Number of results at iteration #', i, ": ", len(lists))
        load_more[0].click()
        time.sleep(1)

    links = [div.get_attribute('data-href') for div in driver.find_elements_by_class_name('more-article')]
    print('Total results: ', len(links))
    links = list(set(links))
    print('Number of results after removing duplicates: ', len(links))

    all_films = {}
    print("Going through each Top 10 List:")
    for link in tqdm(links):
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find_all('h1')[0].contents[0]
        name = name[ : name.find("Top") - 3]
        directors = [tag.string for tag in soup.find_all('h5', class_ = 'editorial-film-listitem__director')]
        titles = [tag.string for tag in soup.find_all('h3', class_ = 'editorial-film-listitem__title')]
        for idx, title in enumerate(titles):
            if title not in all_films:
                obj = {}
                obj["title"] = title
                obj["director"] = directors[idx]
                obj["names"] = [name]
                obj["count"] = 1
                all_films[title] = obj
            else:
                all_films[title]["names"].append(name)
                all_films[title]["count"] += 1
            
    return all_films

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--count', required=False, help='Print movies that were picked by <count> or more people')
    ap.add_argument('--info', required=False, help='Print information on this film.')
    count = vars(ap.parse_args())['count']
    if count is not None:
        count = int(count)
    title = vars(ap.parse_args())['info']
    if title is not None:
        title = str(title)

    if not os.path.isfile('films.json'):
        all_films = scrape_criterion()
        sorted_films = [all_films[key] for key in sorted(all_films, key=lambda item:all_films[item]['count'], reverse=True)]
        with open("films.json", "w") as outfile:  
            json.dump(sorted_films, outfile) 
        
    with open("films.json", "r") as infile:
        sorted_films = json.load(infile)
        # info mode
        if title is not None:
            films = {film['title']: film for film in sorted_films}
            print('Title:', films[title]['title'])
            print('Director:', films[title]['director'])
            print('Count:', films[title]['count'])
            chosen = ''
            for person in films[title]['names']:
                chosen += person + ', '
            chosen = chosen[ : -2]
            print('Chosen By:', chosen)
        if count is not None and title is not None:
            print()
        # count mode
        if count is not None:
            print("Films chosen by over", count, "people were:")
            for film in sorted_films:
                if film['count'] >= count:
                    print(film['title'])
                else:
                    break

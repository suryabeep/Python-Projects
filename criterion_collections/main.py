from bs4 import BeautifulSoup
import requests
import argparse
import json
import os.path
from tqdm import tqdm

def scrape_criterion():
    lists_home_url = 'https://www.criterion.com/current/category/8-top-10-lists'

    response = requests.get(lists_home_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    top_tens_links = [div.get('data-href') for div in soup.find_all('div', class_="more-article")]

    all_films = {}
    print("Going through each Top 10 List:")
    for link in tqdm(top_tens_links):
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
    ap.add_argument('--count', required=True, help='Print movies that were picked by <count> or more people')
    count = int(vars(ap.parse_args())['count'])
    
    if not os.path.isfile('films.json'):
        all_films = scrape_criterion()
        with open("films.json", "w") as outfile:  
            json.dump(all_films, outfile) 
        
    with open("films.json", "r") as infile:
        all_films = json.load(infile)
        for film in all_films:
            if all_films[film]["count"] >= count:
                print(all_films[film])
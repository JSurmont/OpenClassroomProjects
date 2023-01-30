import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"

requete = requests.get(url)

page = requete.content

soup = BeautifulSoup(page, 'html.parser')


def extract_in_array(soupe, tag_name, class_name) :
    return [text.string for text in soupe.find_all(tag_name, class_=class_name)]

titre_text = extract_in_array(soup, 'a', 'gem-c-document-list__item-title')

descriptions_text = extract_in_array(soup, 'p', 'gem-c-document-list__item-description')

with open("data.csv", 'w') as csv_file :
    writer = csv.writer(csv_file, delimiter='|')

    writer.writerow(["titre", "description"])

    for titre, description in zip(titre_text, descriptions_text) :
        row = [titre, description]

        writer.writerow(row)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from dateutil.parser import parse
import psycopg2
from sqlalchemy import create_engine

url = 'https://letterboxd.com/reviews/popular/this/year/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

film_list = soup.find(class_='film-list clear film-details-list no-title')
if not film_list:
    print("Film list not found!")
    exit()

popular_review = film_list.find_all('li')

data = []

for film in popular_review:
    # Extract reviewer
    reviewer = film.get('data-owner', 'No reviewer found')

    # Extract title
    title_element = film.find('h2', class_='headline-2 prettify')
    title = title_element.find('a').text.strip() if title_element and title_element.find('a') else 'No title found'

    # Extract watched date
    review_date_element = film.find('span', class_='date')
    review_date = review_date_element.text.strip() if review_date_element else 'No date found'

    # Extract rating
    rating_element = film.find('span', class_='rating')
    if rating_element:
        rating_text = rating_element.text.strip()
        rating = rating_text.count('★') + (0.5 if '½' in rating_text else 0)
    else:
        rating = None

    review_content_element = film.find('div', class_='body-text -prose collapsible-text')
    if review_content_element:
        review_paragraph = review_content_element.find('p')
        review_text = review_paragraph.text.strip() if review_paragraph else 'No review content'
    else:
        review_text = 'No review content'

    likes_element = film.find('p', class_='like-link-target')
    if likes_element:
        likes = int(likes_element.get('data-count', 0))
    else:
        likes = 0

    data.append({
        'Reviewer': reviewer,
        'Title': title,
        'Date': review_date,
        'Rating': rating,
        'Review': review_text,
        'Likes': likes
    })

df = pd.DataFrame(data)

def parse_date(row):
    try:
        date = parse(row, fuzzy_with_tokens=True)[0]
        return date.strftime('%Y-%m-%d')
    except:
        return np.nan

if 'Date' in df.columns:
    df['Date'] = df['Date'].apply(parse_date)
else:
    print("Column Date not found.")

df.to_csv('popular_reviews.csv', index=False)

df
# Letterboxd Review Scraper

A Python script to scrape popular movie reviews from Letterboxd.com. This tool extracts review data including reviewer names, movie titles, ratings, review content, and like counts, then saves them to a CSV file and store to BigQuery.

## Features

- Scrapes popular reviews from Letterboxd's current year
- Extracts key information:
  - Reviewer username
  - Movie title
  - Review date
  - Rating (including half stars)
  - Review content
  - Number of likes
- Automatically formats dates for consistency
- Exports data to CSV format
- Storing to BigQuery

## Prerequisites

Make sure you have Python 3.6+ installed and the following packages:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
pip install numpy
pip install python-dateutil
pip install psycopg2
pip install sqlalchemy
```

## Installation

1. Clone this repository or download the script:
```bash
git clone https://github.com/fajri-yanti/LetterBox-Popular-Review
cd webscrapiingletterbox
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Basic usage:
```python
python webscrapingletterbox.py
```

This will:
- Scrape the most recent popular reviews from Letterboxd
- Process and clean the data
- Save the results to `popular_reviews.csv`

## Data Format

The script creates a CSV file with the following columns:

- `Reviewer`: Username of the review author
- `Title`: Name of the movie
- `Date`: Date the review was posted (YYYY-MM-DD format)
- `Rating`: Movie rating (0-5 stars, including half stars)
- `Review`: Full text of the review
- `Likes`: Number of likes the review received

## Code Structure

```python
# Main components:
1. Web scraping setup (requests & BeautifulSoup)
2. Data extraction from HTML
3. Date parsing and formatting
4. DataFrame creation and cleaning
5. CSV export
6. Store to BigQuery
```

## Error Handling

The script includes error handling for:
- Missing webpage elements
- Invalid dates
- Missing review content


## Database



## Limitations

- Only scrapes the first page of popular reviews
- Respects Letterboxd's HTML structure (may need updates if site changes)
- Date parsing assumes English language dates

## Future Improvements

Potential enhancements:
1. Multi-page scraping
2. Rate limiting for respectful scraping
4. Additional metadata extraction
5. Error logging


## Legal Note

Before using this scraper, make sure to:
1. Check Letterboxd's robots.txt
2. Review their terms of service
3. Implement appropriate rate limiting
4. Consider using their official API if available

## Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit pull requests



## Disclaimer

This tool is for educational purposes only. Be responsible when scraping websites and respect the site's terms of service.

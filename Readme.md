# Financial News Web Scraping Project

This project extracts financial headlines from Moneycontrol and stores them in CSV files for later analysis. It includes historical general-finance news as well as stock-specific stories.

## Objective

Gather relevant financial updates by scraping Moneycontrol for a list of stocks and saving their recent headlines.

## Tools and Technologies Used

- **Python** for scripting
- **BeautifulSoup** and **requests** for scraping
- **Pandas** for tabular analysis

## Usage

1. Clone the repository.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Use the provided notebooks or scripts to scrape Moneycontrol for the stocks you care about.

### Quick dataset summary

After scraping, run the helper script to inspect the resulting CSV (defaults to `news_data.csv`):

```bash
python analyze_news.py  # or specify a path like python analyze_news.py news_data_combined_input.csv
```

Sample output:

```
News dataset summary
-------------------
Total articles: 120
Articles with valid dates: 118
Coverage window: 2023-06-15 to 2023-12-18
Average title length: 72.4 characters

Articles per day:
  2023-12-17: 12
  2023-12-18: 30
  ...

Top 10 title words:
  market: 9
  india: 7
 ...
```

Use `--top-words N` to customize the number of title keywords shown.

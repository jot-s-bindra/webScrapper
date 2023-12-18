# Financial News Web Scraping Project

This project is aimed at extracting financial news from Moneycontrol using web scraping techniques with BeautifulSoup. The goal is to fetch both general financial news and stock-specific news for a list of stocks and retrieve their headlines over the last six months.

## Objective

The main objective of this project is to gather relevant financial news, including both general financial updates and stock-specific news, by scraping the Moneycontrol website. It accepts a list of stock IDs or names as input and returns the headlines related to these stocks for the past six months.

## Tools and Technologies Used

- **Python:** Programming language used for the project.
- **BeautifulSoup:** Python library for web scraping.
- **Requests:** HTTP library for making requests to web pages.
- **Pandas:** Data manipulation library used for handling and organizing scraped data.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Provide a list of stock IDs or names as input to retrieve their headlines.

Example Usage:

```python

stocks_to_fetch = ['TCS', 'AAPL', 'GOOGL']  # Replace with actual stock IDs/names

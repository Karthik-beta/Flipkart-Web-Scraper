# Flipkart Web Scraper

Welcome to the Flipkart Web Scraper! This project is an efficient and reliable web scraper that collects data from the Flipkart website. Specifically, the scraper collects information about mobile phones that cost less than 50000 rupees, allowing you to quickly and easily gather data on affordable smartphones. 

## Methodology

This scraper was built using Python 3, leveraging the powerful libraries of pandas, requests, and BeautifulSoup. These libraries provide a wide range of tools and functionality, allowing you to easily and efficiently manipulate data from the web. The scraper follows a simple methodology: it sends a GET request to the Flipkart website with the appropriate search parameters, and then uses BeautifulSoup to parse the HTML response and extract the relevant data. The data is then stored in a Pandas DataFrame and written to a CSV file. 

## Requirements

To use this scraper, you will need to have the following libraries installed:

- pandas
- requests
- BeautifulSoup

You can install these libraries using pip. For example:

```
pip install pandas requests beautifulsoup4
```

## Usage

Using the Flipkart Web Scraper is incredibly easy. Simply run the `Web_Scraper.py` file, and the script will scrape data from pages 2 to 4 of the search results, storing the data in a CSV file called `flipkart_mobile_under_50000.csv`.

If you would like to modify the search results that the scraper collects data from, you can edit the URL in the `url` variable on line 10 of the script. Additionally, you can modify the range of pages to scrape by changing the arguments to the `range` function on line 12 of the script.

## Contributing

I welcome contributions to this project! If you have any suggestions or improvements, please open an issue or submit a pull request on GitHub. Your contributions will help make this web scraper even better!


# Import the required libraries
import pandas as pd 
import requests
from bs4 import BeautifulSoup

# Initialize empty lists to store the scraped data
Product_name = []
Prices = []
Description = []
Reviews = []

# Loop through pages 2 to 4 of the search results
for i in range(2, 4):
     # Construct the URL for the current page
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+50000%7CMobiles&requestId=ed4c8693-8722-4d55-be6e-ebbd9fe376fe&as-searchtext=mobiles+under+50000&page="+str(i)

    # Send a GET request to the URL and obtain the HTML content
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div" , class_ = "_1YokD2 _3Mn1Gg")

    # Find the HTML element that contains the product names
    names = box.find_all("div" , class_ = "_4rR01T")
    
    # Extract the product names and append them to the Product_name list
    for i in names:
        name = i.text
        Product_name.append(name)

    # print(Product_name)

    
    # Find the HTML element that contains the product prices
    prices = box.find_all("div" , class_ = "_30jeq3 _1_WHN1")

    # Extract the product prices and append them to the Prices list
    for i in prices:
        name = i.text
        Prices.append(name)

    # print(Prices)

    # Find the HTML element that contains the product descriptions
    desc = box.find_all("ul" , class_ = "_1xgFaf")

    # Extract the product descriptions and append them to the Description list
    for i in desc:
        name = i.text
        Description.append(name)

    # print(Description)


    # Find the HTML element that contains the product reviews
    reviews = box.find_all("div" , class_ = "_3LWZlK")

    # Extract the product reviews and append them to the Reviews list
    for i in reviews:
        name = i.text
        Reviews.append(name)

    # print(Reviews)

# Combine the lists into a pandas DataFrame
df = pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
# print(df)

# Save the DataFrame to a CSV file
df.to_csv("flipkart_mobile_under_50000.csv")
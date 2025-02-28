import requests
from bs4 import BeautifulSoup
import csv


URL = URL = "https://www.ebay.com/sch/i.html?_nkw=laptops"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

def get_product_data(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    
    for item in soup.find_all("div", class_="product-card"):  # Adjust based on website structure
        name = item.find("h2", class_="product-title").text.strip() if item.find("h2", class_="product-title") else "N/A"
        price = item.find("span", class_="price").text.strip() if item.find("span", class_="price") else "N/A"
        rating = item.find("span", class_="rating").text.strip() if item.find("span", class_="rating") else "N/A"
        
        products.append([name, price, rating])
    
    return products

def save_to_csv(data, filename="products.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Rating"])
        writer.writerows(data)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    product_data = get_product_data(URL)
    if product_data:
        save_to_csv(product_data)

from bs4 import BeautifulSoup
import requests
import argparse
import json
import os
from urllib.parse import urlparse
import urllib.robotparser
from models import Book
from sqlalchemy.ext.declarative import declarative_base
from database import Base,DBSession,engine

Base.metadata.bind = engine
session = DBSession()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/118.0 Safari/537.36"
    }
def save_to_db(books):
    print(f"Attempting to save {len(books)} books")
    for i, book in enumerate(books):
        print(f"Processing book {i+1}: {book.get('title', 'Unknown')}")
        try:
            book_entry = Book(
                title=book['title'],
                url=book['url'],
                category=book['category'],
                price=book['price']
            )
            session.add(book_entry)
        except Exception as e:
            print(f"Error creating book entry {i+1}: {e}")
            raise
    
    print("Committing to database...")
    session.commit()
    print("Database commit successful")
def can_fetch(url, user_agent="*"):
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp.can_fetch(user_agent, url)
    
def scraping(url,books_data):
    html_doc = requests.get(url,headers).text
    soup = BeautifulSoup(html_doc, 'lxml') 
    books = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    
    for book in books:
        title = book.h3.a['title']
        Book_url = book.h3.a['href']  
        Book_url = "https://books.toscrape.com/catalogue/" + Book_url
        catalogue_html = requests.get(Book_url,headers).text
        catalogue_soup = BeautifulSoup(catalogue_html, 'lxml')
        catalogue = catalogue_soup.find('ul', class_='breadcrumb')
        category = catalogue.find_all('li')[2].a.text
        
        price = book.find('p', class_='price_color').text.replace('Â', '')
        books_data.append({
            'title': title,
            'url': Book_url,
            'category': category,
            'price': price
        })
    return books_data
    

def scrape_books(num_pages=1):
    books_data = []
 
    base_urls = "https://books.toscrape.com/catalogue/page-{}.html"
    for n in range(1, num_pages + 1):
        base_url = base_urls.format(n)
        if can_fetch(base_url, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/118.0 Safari/537.36"):
            books_data = scraping(base_url,books_data)
        else:
            print(f"❌ Disallowed by robots.txt: {base_url}")
            break
           
            
    return books_data
def save_to_json(books, filename='books.json'):
        os.makedirs('samples', exist_ok=True)
        filename = "samples/scraped.json"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                try:
                    old_data = json.load(f)
                except json.JSONDecodeError:
                    old_data = []
        else:
            old_data = []
            
        old_data.extend(books)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(old_data, f, indent=2, ensure_ascii=False)    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pages', type=int, default=1)
    parser.add_argument('--db',action='store_true')
    args = parser.parse_args()
    books = scrape_books(num_pages=args.pages)
    save_to_json(books)
    if args.db:
        save_to_db(books)
        




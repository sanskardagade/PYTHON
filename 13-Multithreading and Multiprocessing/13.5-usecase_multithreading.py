'''
Real-World Example: Multithreading for I/O-Bound Tasks
Scanerio : Web Scrapping 
Web Scrapping often involves making numerous network rwquest to fetch web pages. These tasks are I/O-bound because they spend a lot of time waiting for responses from server. Multithreading can significantly improve the performance of web scrapping by allowing multiple pages to be made  fetch concurrently.

'''

'''
https://docs.langchain.com/oss/python/langchain/overview
https://docs.langchain.com/oss/python/langchain/install
https://docs.langchain.com/oss/python/langchain/philosophy
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://docs.langchain.com/oss/python/langchain/overview',
    'https://docs.langchain.com/oss/python/langchain/install',
    'https://docs.langchain.com/oss/python/langchain/philosophy'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()   # ✅ start the thread itself

for thread in threads:
    thread.join()

print("All web pages fetched.")

""" 
Web scraping is the process of automatically extracting data from websites using software or scripts
"""
# let's implement the multi threading concept in web scarping
# urls

import threading
from bs4 import BeautifulSoup
import requests

urls = [ 
    'https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/',
    'https://medium.com/@superfastpython/python-processpoolexecutor-7-day-crash-course-71cf062409d2',
    'https://www.geeksforgeeks.org/python/multiprocessing-python-set-1/',
    'https://www.python.org/'
]

# function to fetch the data
def fetch_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser') #parsing HTML and XML documents.
    print(f'Total number of character fetch: {len(soup.text)} from {url}')

# list of threads
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_data,args=(url,)) #creating the threads
    threads.append(thread) #appending the threads in threads list
    thread.start() 

for thread in threads:
    thread.join()

print("All the data are fetch")

# output:
# Total number of character fetch: 7025 from https://www.python.org/
# Total number of character fetch: 33850 from https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/
# Total number of character fetch: 26850 from https://www.geeksforgeeks.org/python/multiprocessing-python-set-1/
# Total number of character fetch: 15164 from https://medium.com/@superfastpython/python-processpoolexecutor-7-day-crash-course-71cf062409d2
# All the data are fetch
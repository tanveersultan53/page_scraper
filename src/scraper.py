import requests
from bs4 import BeautifulSoup as bs
import os
import random
import string



def get_url_content(url='https://www.vocabulary.com/dictionary/tutorial'):
    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'})
    # convert to beautiful soup
    soup = bs(response.content)
    # passing list to find/find_all() function:-

    return soup
    # find_head = soup.find()

    for strong_tag in soup.find_all('body'):
        print(strong_tag.text)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


def download_file(soup):
    file_name = get_random_string(8)
    with open('readme.txt', 'w') as f:
        for strong_tag in soup.find_all('body'):
            f.write(strong_tag.text.strip())
            f.write('\n')

    with open('readme.txt') as input_file, open(f'{file_name}.txt', 'w') as outfile:
        for line in input_file:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty line. Write it to output

    if os.path.exists("readme.txt"):
        os.remove("readme.txt")  # one file at a time
    
    return file_name
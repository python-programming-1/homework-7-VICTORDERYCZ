import requests
from bs4 import BeautifulSoup
import os
from time import sleep

# get main website
url = 'https://www.gocomics.com/pearlsbeforeswine/2019/08/21'
for i in range(10):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text)

    # find <div id=comic>
    comic_div = soup.select('div.comic__image')

    # find image url
    image_url = comic_div[0].contents[3].contents[1].next.attrs['src']
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    # save image url
    image_file = open(os.path.basename(image_url) + '.png', 'wb') # save just the file image name
    for chunk in image_res.iter_content(100000):
        image_file.write(chunk)
    
    image_file.close()

    # get prev url
    prev_link = soup.select('a.fa.btn.btn-outline-secondary.btn-circle.fa-caret-left.sm.js-previous-comic[role="button"]')[0]
    url = 'http://gocomicsgo.com' + prev_link.get('href')
    print(url)
    sleep(1)
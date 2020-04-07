import requests
import time
import json
from bs4 import BeautifulSoup

import discord
import config

links = []
skus = []
names = []

#get SKUs, Products name from URL
with open('links.txt','r') as f:
    for line in f:
        link = line.strip()
        links.append(link)

        r = requests.get(link)
        bsObj = BeautifulSoup(r.text, 'html.parser')

        name = bsObj.find("h1", {'itemprop':'name'}).text
        names.append(name)

        sku = bsObj.find("ul", {"class":"product-numbers"}).findAll("li")[1].find("span").text
        skus.append(sku)

        print("item: {} \t sku: {} \n link: {}".format(name, sku, link))

zipList = []
with open('zipcode.txt','r') as f:
    zipList = f.read().splitlines()

def main():
    while True:
        for zip in zipList:
            for i in range(len(links)):
                    checkInstore(zip, names[i], skus[i], links[i])


def checkInstore(zip, name, sku, link):
    url = 'https://availability.dickssportinggoods.com/ws/v2/omni/stores?addr={}&radius=100&uom=imperial&lob=dsg&sku={}&res=locatorsearch&qty=1'.format(zip, sku)
    try:
        r = requests.get(url, timeout=5, headers=config.header, proxies=config.proxy).json()
        #print(r)
    except:
        checkInstore(zip, name, sku, link)
        return

    if 'data' not in r:
        return

    if(len(r['data']['results']) == 0):
        return

    result = r['data']['results']
    for i in range(len(result)):
        parseLocation(name, link, sku, result[i], zip)

def parseLocation(name, link, sku, result, zip):
    zipcode = result['store']['zip']
    location = result['store']['street1']
    qty = result['skus'][0]['qty']
    ats = qty['ats']

    message = time.strftime('%a %H:%M:%S') + " Curbside\nItem: {}\nAvailability: {}\nlocation: {} \t zipcode: {}\n{}".format(name, str(qty), location, zipcode, link)
    if(int(ats) > 0):
        discord.sendDiscord(message, 'curbside', sku, zip)
    #else:
        #print(message)


if __name__ == "__main__":
    main()

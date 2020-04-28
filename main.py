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
        try:
            link = line.strip()

            r = requests.get(link)
            bsObj = BeautifulSoup(r.text, 'html.parser')

            name = bsObj.find("h1", {'itemprop':'name'}).text
            sku = bsObj.find("ul", {"class":"product-numbers"}).findAll("li")[1].find("span").text
        except:
            print("bad url: {}".format(link))
            continue

        names.append(name)
        links.append(link)
        skus.append(sku)

        print("item: {} \t sku: {} \n link: {}".format(name, sku, link))

    links.append("https://www.dickssportinggoods.com/p/bowflex-selecttech-552-dumbbells-16bfxuslcttchdmbbslc/16bfxuslcttchdmbbslc")
    names.append("Bowflex selecttech 552")
    skus.append("11465449")

zipList = []
with open('zipcode.txt','r') as f:
    zipList = f.read().splitlines()

def main():
    while True:
        for zip in zipList:
            for i in range(len(links)):
                while(not checkInstore(zip, names[i], skus[i], links[i])):
                    continue


def checkInstore(zip, name, sku, link):
    url = 'https://availability.dickssportinggoods.com/ws/v2/omni/stores?addr={}&radius=100&uom=imperial&lob=dsg&sku={}&res=locatorsearch&qty=1'.format(zip, sku)
    try:
        r = requests.get(url, timeout=5, headers=config.header, proxies=config.proxy).json()
        print(zip, r)
    except:
        return False

    if 'data' not in r:
        return True

    if(len(r['data']['results']) == 0):
        return True

    result = r['data']['results']
    for i in range(len(result)):
        parseLocation(name, link, sku, result[i], zip)
    return True

def parseLocation(name, link, sku, result, zip):
    try:
        zipcode = result['store']['zip']
        location = result['store']['street1']
        qty = result['skus'][0]['qty']
        ats = qty['ats']

        message = time.strftime('%a %H:%M:%S') + " Curbside\nItem: {}\nAvailability: {}\nlocation: {} \t zipcode: {}\n{}".format(name, str(qty), location, zipcode, link)
        if(int(ats) > 0):
            discord.sendDiscord(message, 'curbside', sku, zip)
    except:
        return False
    return True
    #else:
        #print(message)


if __name__ == "__main__":
    main()

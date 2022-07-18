from enum import auto
from sys import exit
import requests, random

foundList = []
numberList = 100000000

# Increases count
def numbers():
    while numberList < 300000000:
        numberList+=1
        return numberList

# Takes numbers and combines it with prefix URL
def combinedURL(number):
    urlPrefix = 'https://lrps.wgu.edu/provision/'
    urlComplete = urlPrefix+number
    return urlComplete

# Temporary array keeping track of valid urls
def ifFound(code, url):
    if code == 200:
        for a in foundList:
            if url != a:
                foundList.append(url)

# Prints the final foundList array vertically
def printStuff():
    for i in foundList:
        print('Valid links: ' + i)

# Automated search based on wordlists
def automatedBuilder():
    automatedInput = urlTemplate(alist, blist, clist)
    resp = requests.get(automatedInput.combinedURL())
    print(resp.status_code)
    ifFound(resp.status_code, automatedInput.combinedURL())

    printStuff()

automatedBuilder()
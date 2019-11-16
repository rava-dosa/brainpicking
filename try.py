import requests
from bs4 import BeautifulSoup


def getmemeat(soup):
    ret1=[]
    archive=soup.find("div", {"id": "recent_archives"})
    for x in archive.find_all('h5'):
        temp=[]
        temp1=x.find_all('a')
        temp.append(temp1[0].getText())
        temp.append(temp1[0].get('href'))
        ret1.append(temp)
    return ret1


def getnexturl(soup):
    try:
        archive=soup.find("a", {"class": "nextpostslink"})
        return archive.get('href')
    except:
        return None

def getmefile(url1):
    a=requests.get(url1)
    a=a.text
    soup = BeautifulSoup(a, 'html.parser')
    ret1=getmemeat(soup)
    f=open("brainpick.md","a+")
    for x in ret1:
        tempx="1. [{}]({})".format(x[0],x[1])
        f.write(tempx+"\n")
    f.close()
    return soup

def main1():
    url1="https://www.brainpickings.org/{}/"
    for x in reversed(range(2006,2019)):
        f=open("brainpick.md","a+")
        f.write("## {}\n".format(x))
        f.close()
        soup=getmefile(url1.format(x))
        temp1=getnexturl(soup)
        while(temp1 is not None):
            print(temp1)
            soup=getmefile(temp1)
            temp1=getnexturl(soup)
        print("{x} done".format(x))

main1()
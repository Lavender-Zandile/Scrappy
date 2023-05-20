import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.bda-ieo.it/test/Alphabetical.aspx?Lan=Eng&FL=%")
soup = BeautifulSoup(req.content, "html.parser")
trs = soup.find_all("tr", class_ = "testonormale")
# print(type(links))

#empty list to store urls


#loop through the links and append the urks to the list
def getLinks():
    data_list = []
    for tr in trs:
        tds=tr.find_all("td")
        id=tds[0].contents[0]
        aTag=tds[1].find("a")
        link=aTag.get("href")
        name=aTag.contents[0]
        data={}
        data['id']=id
        data['name']=name
        data['link']=link
        data_list.append(data)
    return data_list

print(getLinks())




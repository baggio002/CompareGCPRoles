import requests
from bs4 import BeautifulSoup

URL = "https://cloud.google.com/iam/docs/permissions-reference"
IFRAME_URL = ""

class PermissionRoles:
    # permission = ""
    roles = []

    def print(self):
        print("permission = " + self.permission)
        print(f'roles = {self.roles}')

def getIframeSrc(url):
    return BeautifulSoup(requests.get(url).content, "html.parser").find("iframe")["src"]
    
def getTbodyContent(url):
    return BeautifulSoup(requests.get(url).content, "html.parser").find("tbody")

def loopRoles(content):
    i = 0
    for tr in content.find_all("tr"):
        rps = PermissionRoles()
        rps.permission = tr.find("td")["id"]
        for li in tr.find_all("li"):
            rps.roles.append(li.text)
        

def main():
    IFRAME_URL = getIframeSrc(URL)
    loopRoles(getTbodyContent(IFRAME_URL))

    
if __name__ == "__main__":
    main()

from bs4 import  BeautifulSoup
import  requests
url="https://www.naukri.com/python-software-developer-python-development-jobs?k=python%2C%20python%20software%20developer%2C%20python%20development&nignbevent_src=jobsearchDeskGNB"
content=requests.get(url)
print(content)
# res=BeautifulSoup(content,"html.parser")
# print(rs.)
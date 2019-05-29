import requests
from bs4 import BeautifulSoup
File = open("webscrappy.txt","w")
webpage=requests.get("https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(webpage.content,"html.parser")
lists = []
lists=soup.find_all(attrs={'class':['_3wU53n','tVe95H']})
for i in lists:
        print(i.string)
        File.write("\n"+i.string)
File.close()

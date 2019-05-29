import requests
from bs4 import BeautifulSoup
File = open("webscrappy.txt","w")
webpage=requests.get("url of website with product already serached for then copy and paste the link in here")
#webpage is a requests.get pbject we created to store the response from the get request we sent.
#eg requests.get("https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(webpage.content,"html.parser")
#soup is a beautifulsoup object that we created to store the parsed html content
#html parser is a method in Beautiful soup used for parsing html pages
lists = []
lists=soup.find_all(attrs={'class':['_3wU53n','tVe95H']})
#find_all() is used to find all the tags that fulfill a specific criteria in this scenario that is having classes with names _3wU53n and tVe95H respectively.
#class is the name of classes of the tags you want to print since am using multiple so i created a list for that 
for i in lists:
        print(i.string)
        #i used i.string in order to strip the html tags and just get the plain text contained within the tags
        File.write("\n"+i.string)
        #finally writing the content of the site to a file.
File.close()

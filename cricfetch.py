import subprocess
import urllib2
from bs4 import BeautifulSoup
url="http://www.espncricinfo.com/ci/engine/match/index.html"
page=urllib2.urlopen(url)
soup=BeautifulSoup(page)
g_data1=soup.find_all("div",class_="innings-info-1")
templist=["Otago","Canterbury "]
c=0

for item1 in g_data1:

        x=item1.text
        x=str(x)
        if templist[0] in x:
                break
        if templist[1] in x:
                break
        #print "a"
        c=c+1

x=g_data1[c].text
x=str(x)
words=x.split()
string=''.join(map(str, words))
print string
g_data2=soup.find_all("div",class_="innings-info-2")
x=g_data2[c].text
x=str(x)
words=x.split()
string2=''.join(map(str, words))
print string2
string3=templist[0]+"vs"+templist[1]

subprocess.call(['bash','1.sh',string,string2,string3])

#g_data3=soup.find_all("div",class_="match-status")
#print g_data3[c].text


'''Problem Statement

In this assignment students have to find the frequency of words in a webpage. User can
use urllib and BeautifulSoup to extract text from webpage.

Hint:
from bs4 import BeautifulSoup
import urllib.request
import nltk

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
NOTE:​ ​The​ ​solution​ ​shared​ ​through​ ​Github​ ​should​ ​contain​ ​the​ ​source​ ​code​ ​used​ ​and​'''

from bs4 import BeautifulSoup
import urllib
from collections import Counter
import nltk

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
 
text = soup.get_text(strip=True)


tokens = [t for t in text.split()]
Counter(tokens)
freq = nltk.FreqDist(tokens)
 
for key,val in Counter(tokens).items():
    print (str(key) + ':' + str(val))
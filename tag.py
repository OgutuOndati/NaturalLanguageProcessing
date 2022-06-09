import urllib.request #url handling
from bs4 import BeautifulSoup #parsing or handling html files

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

#get the info from the website
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/spaceX')
html = response.read()

soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip=True)


tokens = [t for t in text.split()]

sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):

        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' +str(val))
freq.plot(20, cumulative=False)
        

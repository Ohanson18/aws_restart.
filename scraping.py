import requests
from bs4 import BeautifulSoup
r = requests.get('https://aws.amazon.com/blogs/security/learn-and-use-13-aws-security-tools-to-implement-sec-recommended-protection-stored-customer-data-cloud/')
soup = BeautifulSoup(r.text,'html.parser')

for link in soup.find_all('a'):
 if 'blog' in str(link):
  print(link.get('href'))







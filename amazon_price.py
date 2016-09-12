import bs4,requests
url = input("Enter url ")
res = requests.get(url=url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

pr=soup.select('#priceblock_ourprice')
if len(pr) == 0:
    pr=pr=soup.select('#priceblock_saleprice')

pr=pr[0].text.strip()
print("The price is %s" % (pr))

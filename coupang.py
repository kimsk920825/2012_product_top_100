import requests, openpyxl
from bs4 import BeautifulSoup

res = requests.get('https://www.coupang.com/np/categories/194276?listSize=120&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&rating=0')
soup = BeautifulSoup(res.content, 'html.parser')
data =soup.select('dl.baby-product-wrap')

#print(data)
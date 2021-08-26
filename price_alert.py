
import requests
from bs4 import BeautifulSoup, element


url="https://www.amazon.in/OnePlus-Nord-Sierra-128GB-Storage/dp/B097RDVDL2/ref=lp_22424253031_1_1"
tag_name='span'
query={"class":"a-size-medium a-color-price priceBlockDealPriceString"}



responce=requests.get(url)
content=responce.content
soup=BeautifulSoup(content,'html.parser')
elements=soup.find(tag_name,query)

string_price=elements.text

print(string_price)
# <span id="priceblock_dealprice" class="a-size-medium a-color-price priceBlockDealPriceString">₹29,999.00</span>
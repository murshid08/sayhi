__author__="jslvtr"


import requests
from bs4 import BeautifulSoup


request=requests.get("https://www.flipkart.com/huntindia-high-power-long-life-flashlight-rechargeable-two-bulb-led-torch/p/itma87ac51d14942?pid=TOHGYT9FYATBHCKZ&lid=LSTTOHGYT9FYATBHCKZYGQCLU&marketplace=FLIPKART&store=jhg%2Fyqn%2Fdb9&srno=b_1_1&otracker=hp_reco_Monsoon%2BMust-haves_3_4.dealCard.OMU_cid%3AS_F_N_jhg_yqn_db9__d_50-100__NONE_ALL%3Bnid%3Ajhg_yqn_db9_%3Bet%3AS%3Beid%3Ajhg_yqn_db9_%3Bmp%3AF%3Bct%3Ad%3B_3&otracker1=hp_reco_SECTIONED_manualRanking_personalisedRecommendation%2FC5_Monsoon%2BMust-haves_DESKTOP_HORIZONTAL_dealCard_cc_3_NA_view-all_3&fm=personalisedRecommendation%2FC5&iid=en_fLbY1MK9wRjtZMbmWtSCUBE3UVIbprv5uB4ay9PTzxTIZwhb7lD5KbWF7u6ilhyTJhTKLiGYjxalqIl%2BEtOwbA%3D%3D&ppt=hp&ppn=homepage&ssid=bwtsg52fc00000001627992405440")
content=request.content
print(content)
soup=BeautifulSoup(content,'html.parser')
data=soup.find("div",{"class":"_30jeq3 _16Jk6d"})
price=data.text.strip()

acc_price=price[1:]



# <div class="_30jeq3 _16Jk6d">₹499</div>
# <div class="_30jeq3 _16Jk6d">₹1,15,900</div>
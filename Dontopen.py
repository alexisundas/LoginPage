import requests
from bs4 import BeautifulSoup
import csv 

webpages = ['https://t.me/Dx15LINSTAHERO',
'https://t.me/touchdx50',
'https://t.me/GROWTHBOX20',
'https://t.me/Dx20LINSTAHERO',
'https://t.me/sonic_dx5',
'https://t.me/instagirlsdx10lc',
'https://t.me/Dx30LINSTAHERO',
'https://t.me/Dx8LCINSTAHERO',
'https://t.me/Dx10lcinstahero',
'https://t.me/Dx28linstalegend',
'https://t.me/Dx30BOOSTIFY',
'https://t.me/Dx35LINSTALEGEND',
'https://t.me/organic45likes',
'https://t.me/speeddx8',
'https://t.me/Dx50linstalegend',
'https://t.me/organic100likes',
'https://t.me/GROWTH45BOX',
'https://t.me/Dx3TopBoosters',
'https://t.me/Dx5TopBoosters',
'https://t.me/Dx30LikesTopBoosters',
'https://t.me/HYPE50GRAM',
'https://t.me/HYPE60GRAM',
'https://t.me/GROWTH8BOX',
'https://t.me/GROWTH18BOX',
'https://t.me/GROWTHBOX60',
'https://t.me/GROWTHBOX15',
'https://t.me/GROWTHBOX10',
'https://t.me/ActivesEngagementDX30C',
'https://t.me/ActivesEngagementDX50',
'https://t.me/GROWTHBOX7',
'https://t.me/luxesocial10',
'https://t.me/FivestarsgramDx5LC',
'https://t.me/organic20likes',
'https://t.me/instaorganicdx20likes',
'https://t.me/Beauty_4all',
'https://t.me/FlamingoLikesLCDx10',
'https://t.me/beauty4AllDX15Comment',
'https://t.me/FivestarsgramDx30L',
'https://t.me/organic7comments',
'https://t.me/girlsclub30',
'https://t.me/Dx30Mosquito',
'https://t.me/powerlikesboost',
'https://t.me/dx50rgs',
'https://t.me/Dx50fitness',
'https://t.me/Dx30NEVERLINE',
'https://t.me/pushgroupdx10new',
'https://t.me/kdengagementlike',
'https://t.me/EmaraldComments',
'https://t.me/InstaorganicDX25likes',
'https://t.me/viralgrow',
'https://t.me/luxesocialdx3',
'https://t.me/luxex20',
'https://t.me/luxex10',
'https://t.me/Power1k',
'https://t.me/engagementlikes50',
'https://t.me/GET_INSTAGRAM_LIKES_DX10',
'https://t.me/digitalfabricatormarket',
'https://t.me/pushgroupdx50',
'https://t.me/instaorganicdx15supercomments',
'https://t.me/Dx25NEVERLINE',
'https://t.me/Dx70Mosquito',
'https://t.me/Dx10Mosquito',
'https://t.me/Dx7Mosquito',
'https://t.me/Dx15NEVERLINE',
'https://t.me/FlashDx27',
'https://t.me/pushdx7',
'https://t.me/LeosLeosLeo',
'https://t.me/instaorganicdx10likes',
'https://t.me/dx20power',
'https://t.me/smacdx15',
'https://t.me/GET_INSTAGRAM_LIKES_DX20',
'https://t.me/Dx20NEVERLINE',
'https://t.me/Tornadodx50',
'https://t.me/Dx25BOOSTIFY',
'https://t.me/libertydxgroup',
'https://t.me/HiveDX5Comments',
'https://t.me/Dx10group',
'https://t.me/dx10kilogramlikes',
'https://t.me/legenddx30',
'https://t.me/instaorganicdx5comments',
'https://t.me/cloudlikesdx24',
'https://t.me/srvip5k',
'https://t.me/luxesocialdx8',
'https://t.me/HugeGainDx5Group',
'https://t.me/empowerDX10',
'https://t.me/BlazeDx10',
'https://t.me/SNTDX7',
'https://t.me/dx10likesi',
'https://t.me/dx20l',]

group_list = []

def group_names():
    for onesite in webpages:
        url = onesite
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('div', class_='tgme_page_title')
        for text in title:
            if text == None:
                continue
            result = soup.find('span')
        group_list.append(result.text + "," + url)

group_names()

def url():
    for onesite in webpages:
        url = onesite
        return url

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['Group Name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for page in group_list:
        writer.writerow({'Group Name': page})

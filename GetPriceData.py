import requests
import pandas as pd
from re import search
from bs4 import BeautifulSoup


whisky_basic = pd.read_csv('whisky.csv',header=0)
distrillery = whisky_basic['Distillery'].tolist()
distrillery_len_plus = [i for i in distrillery if len(i.split(' ')) > 1 ]

url1 = "https://www.totalwine.com/spirits/scotch/c/000885?tab=fullcatalog&beerspiritscountrystate=scotland&spiritsvarietaltype=single-malt&spiritsvolume=standard-size-750-ml&pagesize=180"
url2 = "https://www.totalwine.com/spirits/scotch/c/000885?tab=fullcatalog&beerspiritscountrystate=scotland&spiritsvarietaltype=single-malt&spiritsvolume=standard-size-750-ml&pagesize=180&page=2"
url3 = "https://www.totalwine.com/spirits/scotch/c/000885?tab=fullcatalog&beerspiritscountrystate=scotland&spiritsvarietaltype=single-malt&spiritsvolume=standard-size-750-ml&pagesize=180&page=3"
url4 = "https://www.totalwine.com/spirits/scotch/c/000885?tab=fullcatalog&beerspiritscountrystate=scotland&spiritsvarietaltype=single-malt&spiritsvolume=standard-size-750-ml&pagesize=180&page=4"
url5 = "https://www.totalwine.com/spirits/scotch/c/000885?tab=fullcatalog&beerspiritscountrystate=scotland&spiritsvarietaltype=single-malt&spiritsvolume=standard-size-750-ml&pagesize=180&page=5"

urls = [url1, url2, url3, url4, url5]

headers = ['brand','label','vintage','region','price']
whiksy_region = ['Highland','Lowland','Speyside','Islay & Islands']
data = []

for url in urls:
    page = requests.get(url)
    htmltext = page.text.strip()
    soup = BeautifulSoup(htmltext, 'lxml')
    table = soup.find('ul', {'class':'plp-list'})
    info = table.find_all('li')

    for obs in info:
        status = obs.find('div',{'class':'plp-product-buy-limited'}).get_text()
        # Only getting the available whiskies
        if 'Not currently available' not in status:
            row = []
            # This is for obtaining name
            name = obs.find('a',{'class':'analyticsProductName'}).get_text()
            name_elem = name.split(' ')
            if len(name_elem) > 1:
                brand = name_elem[0] + ' ' + name_elem[1]
            else:
                brand = name_elem[0]
            if brand in distrillery_len_plus:
                brand
            elif 'Isle of Jura' in name:
                brand = 'Isle of Jura'
            elif (len(name_elem) > 2 and brand + name_elem[2] in distrillery_len_plus):
                brand = brand + name_elem[2]
            else:
                brand = name_elem[0]
            row.append(brand)
            row.append(name)

            yr = search('\d{3,}', name)
            if yr is not None:
                row.append(None)
            else:
                yr = search('\d{1,2}', name)
                if yr is not None:
                    row.append(yr.group())
                else:
                    row.append(None)
            # This is for obtaining regions
            tag = obs.find('div', {'class':'plp-product-loc'})
            region_labels = []
            for i in tag.find_all('a',{'class':'analyticsRegion'}):
                region_labels.append(i.get_text())
            region = None
            for place in region_labels:
                if place in whiksy_region:
                    region = place
            row.append(region)
            # Obtaining original price
            price_div = obs.find('div',{'class':'plp-product-price-tc'})
            price = price_div.find('span',{'class':'cart-price-strike'})
            # If no discount
            if price is None:
                price = price_div.find('span',{'class':'price'})
            # Get rid of the dollar sign
            price = price.get_text().replace('$','').strip()
            price = price.replace(',','')
            row.append(price)
            data.append(row)

df = pd.DataFrame(data, columns=headers)
df.to_csv('price.csv',index=False)


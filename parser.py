import requests
from bs4 import BeautifulSoup
import json

def get_data(url):
    HEADERS = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'
    }
    
    #Get a page with a list of hotels
    hotels = {}
    for i in range(0, 90, 30):
        r = requests.get(f'https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most&s={i}', headers = HEADERS)
        soup = BeautifulSoup(r.text, 'lxml')

        hotels_cards = soup.find_all('div', class_ = 'hotel_card_dv')

        #Get hotels names and links
        for hotel_url in hotels_cards:
            hotel_name = hotel_url.find(class_ = 'hotel_name').find('b').text
            hotel_url = hotel_url.find('a').get('href')
            hotels[hotel_name] = hotel_url
    
    #Saving links to hotels
    with open('hotels.json', 'w', encoding='utf-8') as file:
        json.dump(hotels, file, indent=4, ensure_ascii=False)

def main():
    get_data('https://www.tury.ru/hotel/most_luxe.php')

if __name__ == '__main__':
    main()
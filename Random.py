import time

from selenium import webdriver
import fake_useragent
from bs4 import BeautifulSoup
from requests import get
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
game = input('Game Name: ')
headers = {'user-agent': fake_useragent.UserAgent().random}
soup = BeautifulSoup(get(f'https://store.steampowered.com/search/?term={game.replace(" ", "+")}', headers=headers).text,
                     'html.parser')

all_url = []
for i in soup.find_all('a'):
    if str(i.get('href')).startswith('https://store.steampowered.com/app/'):
        all_url.append(i.get('href'))


for k, i in enumerate(soup.find_all('span', class_='title')):
    print(f'[{k+1}] {i.contents[0]}')

index = int(input('Enter num: '))

driver = webdriver.Chrome()
driver.get(all_url[index-1])
if 'https://store.steampowered.com/agecheck' in str(driver.current_url):
    Select(driver.find_element(By.XPATH, '//*[@id="ageYear"]')).select_by_visible_text('2003')
    driver.find_element(By.XPATH, '//*[@id="view_product_page_btn"]').click()

driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//*[@id="game_area_purchase_section_add_to_cart_440408"]/div[2]/div').click()

time.sleep(1e6)

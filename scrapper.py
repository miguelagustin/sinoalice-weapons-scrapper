from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager

baseurl = 'https://sinoalice.game-db.tw'
url = 'https://sinoalice.game-db.tw/weapons'
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get(url)
driver.find_element_by_class_name('settingBtn').click()
driver.find_elements_by_class_name('radioBtn')[1].click()
driver.execute_script("el = document.elementFromPoint(200, 200); el.click();")
driver.close()
sleep(8)

soup = BeautifulSoup(driver.page_source)

names = soup.find_all('td', class_='colName')
types = soup.find_all('td', class_='colEqType')
patks = soup.find_all('td', class_='colMaxPAtk')
pdefs = soup.find_all('td', class_='colMaxPDef')
matks = soup.find_all('td', class_='colMaxMAtk')
mdefs = soup.find_all('td', class_='colMaxMDef')
totals = soup.find_all('td', class_='colMaxTotal')
costs = soup.find_all('td', class_='colCost')
coloskills = soup.find_all('td', class_='colGvgSkill')
caidskills = soup.find_all('td', class_='colGvgAidSkill')

with open('sinoalice_weapons.csv', 'w', newline='', encoding='utf-16') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Link', 'Type', 'PATK', 'PDEF', 'MATK', 'MDEF', 'Total', 'Cost', 'Colo.Skill', 'C.Aid Skill'])

    for x in range(len(names)):
        writer.writerow([names[x].a.text, baseurl + names[x].a['href'], types[x].text, patks[x].text, pdefs[x].text,
                         matks[x].text, mdefs[x].text, totals[x].text, costs[x].text, coloskills[x].text,
                         caidskills[x].text])


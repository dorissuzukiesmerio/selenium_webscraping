from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

#create a new instance of Google Chrome:
driver = webdriver.Chrome("./chromedriver") #######CHECK CORRECT PATH
driver.get("https://www.reddit.com/r/learnprogramming/top/?t=month")

print(driver.page_source)
driver.quit()

# options = Options()
# options.add_argument("--window-size=1920,1080")
driver.save_screenshot('screenshot.png')

###########

login_button = driver.find_element_by_class_name('_2tU8R9NTqhvBrhoNAXWWcP')
login_button.click()


###### FILL INFO:

driver.switch_to_frame(driver.find_element_by_class_name('_25r3t_lrPF3M6zD2YkWvZU'))

driver.find_element_by_id("loginUsername").send_keys('USERNAME')
driver.find_element_by_id("loginPassword").send_keys('PASSWORD')

driver.find_element_by_xpath("//button[@type='submit']").click()


#### Extracting the data:
from bs4 import BeautifulSoup
import pandas as pd

titles = []
upvotes=[]
authors = []

# PARSE : put in a separate file:

import BeautifulSoup
import pandas

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

## double-check:

for element in soup.findAll('div', attrs={'class': '_1oQyIsiPHYt6nx7VOmd1sz'}):
   title = element.find('h3', attrs={'class': '_eYtD2XCVieq6emjKBH3m'})
   upvote = element.find('div', attrs={'class': '_3a2ZHWaih05DgAOtvu6cIo'})
   author = element.find('a', attrs={'class': '_23wugcdiaj44hdfugIAlnX'})
   titles.append(title.text)
   upvotes.append(upvote.text)
   authors.append(author.text)


df = pd.DataFrame({'Post title': titles, 'Author': authors, 'Number of upvotes': upvotes})
df.to_csv('posts.csv', index=False, encoding='utf-8')


# https://www.webscrapingapi.com/python-selenium-web-scraper/
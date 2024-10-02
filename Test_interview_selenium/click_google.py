import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url ="https://www.google.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
#locators
#search_box_XPATH ="//div[@class='SDkEP']/div[2]"  #with index
search_box_XPATH ="//div[@class='SDkEP']//textarea[@class='gLFyf']" # (without Index)

#Actions
ele = "hp"
search_box = driver.find_element(By.XPATH, search_box_XPATH)
time.sleep(1)
search_box.send_keys(ele + Keys.ENTER)
imgs = driver.find_elements(By.XPATH,"//img")
print(len(imgs))
#inspect on "I'm Feeling Lucky" button
#driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnI']").click()
#time.sleep(2)
driver.close()
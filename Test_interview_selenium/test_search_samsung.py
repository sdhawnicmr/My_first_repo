import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url ="https://www.amazon.in/"
driver.get(url)
driver.maximize_window()

search_box_Xapth = '//input[@type="text"]'
search_botton_xpath= "//input[@type='submit']"

driver.find_element(By.XPATH,search_box_Xapth).send_keys("samsung")
time.sleep(1)
driver.find_element(By.XPATH,search_botton_xpath).click()
time.sleep(1)

wait = WebDriverWait(driver, 10)

# Wait until the first mobile link is present
link = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='sg-col-inner']//h2/a)[1]")))
time.sleep(2)
l_url = link.get_attribute('href')
time.sleep(2)
print("77897")
print(f"First Samsung Mobile Link: {l_url}")

driver.quit()
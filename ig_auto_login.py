from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

account=''
password=''

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver=webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")
#titles=driver.find_elements(By.CLASS_NAME,"title")
#print(len(titles))
#for title in titles:
#    print(title)
time.sleep(2)
username=driver.find_element(By.NAME,'username')
username.send_keys(account)
userpassword=driver.find_element(By.NAME,'password')
userpassword.send_keys(password)
time.sleep(1)
login=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
login.click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
a=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
a.click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
b=driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
b.click()
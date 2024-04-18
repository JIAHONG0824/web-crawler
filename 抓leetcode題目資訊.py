from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #有了這個selenium開啟的瀏覽器才不會自動關閉
options.add_argument('user-data-dir=C:/Users/user no1/AppData/Local/Google/Chrome/User Data1') #攜帶google登入的資訊 這樣遇到有些登入方式有google的可以省略 還要先去你原本的資料夾複製一個出來
#options.add_argument("--user-data-dir=C:/Users/user no1/AppData/Local/Google/Chrome/User Data")
#options.add_argument("--profile-directory=1"); 
driver=webdriver.Chrome(options=options)
url='https://leetcode.com/problems/remove-element/description/' #更改網址就好
driver.get(url)


WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]"]')))
difficulty=driver.find_element(By.CSS_SELECTOR,'[class="relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-easy dark:text-difficulty-easy"]')
final_text='# '+'`'+difficulty.text+'` '

title=driver.find_element(By.CSS_SELECTOR,'[class="no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]"]')
final_text+='['+title.text+']'+'('+url+')'+'\n'+'### Topics:'

WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="text-body text-text-primary dark:text-text-primary"]')))
button=driver.find_element(By.CSS_SELECTOR,'[class="text-body text-text-primary dark:text-text-primary"]')
button.click()


time.sleep(1) ##這邊超重要 沒有這個會讀不到topics 可能要給他時間緩衝
topics=driver.find_elements(By.CSS_SELECTOR,'[class="no-underline hover:text-current relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-text-secondary"]')
for topic in topics:
    final_text+=' `'+topic.text+'`'
print(final_text)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import urllib.request

def get_images_url(url,folder_path):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True) #有了這個selenium開啟的瀏覽器才不會自動關閉
    options.add_argument('--headless') #無頭模式
    driver=webdriver.Chrome(options=options)

    driver.get(url)

    images = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/section/div[1]/div[3]/div[2]/div[3]/ul/li/div[1]/span')
    images_url = []

    for image in images:
        images_url.append(image.get_attribute('style').split('"')[1])
    driver.quit()
    

    for i in range(len(images_url)):
        urllib.request.urlretrieve(images_url[i], folder_path + '/' + str(i) + '.jpg')
    
    messagebox.showinfo("提醒", "任務已完成！")
    return 


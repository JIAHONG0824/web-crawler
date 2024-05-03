from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def LeetCode(url:str,driver:webdriver.Chrome):
    #獲取LeetCode題目的難度、標題和主題
    try:
        Markdown_text=''

        driver.get(url)
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[class="no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]"]')))
        #獲取標題和難度
        title=driver.find_element(By.CSS_SELECTOR,'[class="no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]"]')
        difficulty=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[4]/div/div[1]/div[2]/div[1]')
        
        
        driver.execute_script("arguments[0].click();",
                            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="text-body text-text-primary dark:text-text-primary"]'))))
        
        Markdown_text+='# '+'`'+difficulty.text+'` '+'['+title.text+']'+'('+url+')'+'\n'+'### Topics:'
        #獲取主題
        WebDriverWait(driver, 5).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'[class="no-underline hover:text-current relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-text-secondary"]')))
        topics=driver.find_elements(By.CSS_SELECTOR,'[class="no-underline hover:text-current relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-text-secondary"]')
        for topic in topics:
            Markdown_text+=' `'+topic.text+'`'

        return Markdown_text
    #如果獲取失敗，則返回'Invalid URL or Element not found'
    except:
        return 'Invalid URL or Element not found'
import requests
from bs4 import BeautifulSoup
import os
import winsound

def download(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')

    #貼圖名稱
    title=soup.find('p',class_='mdCMN38Item01Ttl').text
    #建立資料夾 名字為貼圖名稱
    folder_name=f"{title}/"
    #圖片網址
    images=soup.find_all('span',class_='mdCMN09Image FnPreview')
    image_urls=[]
    for image in images:
        temp=image.get('style')
        image_urls.append(temp[temp.find('https'):temp.find(')')])

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for i in range(len(image_urls)):
        response=requests.get(image_urls[i])
        with open(folder_name+f"{i}.png",'wb') as f:
            f.write(response.content)

if __name__ == '__main__':
    url=input('請輸入網址:')
    download(url)
    winsound.MessageBeep()
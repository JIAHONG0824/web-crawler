from selenium import webdriver
import tkinter as tk
from Get_LeetCode_Markdown import LeetCode
import pyperclip

driver=webdriver.Chrome()
driver.minimize_window()

#退出函數
def Quit():
    driver.quit()
    root.quit()

#生成Markdown函數
def generate_markdown():
    url=url_entry.get()
    markdown_text=LeetCode(url,driver)

    #如果Markdown_text為'Invalid URL or Element not found'，則輸出標籤顯示'Invalid URL or Element not found'，否則輸出標籤顯示'Markdown Generated'
    if markdown_text=='Invalid URL or Element not found':
        output_label.config(text="Invalid URL or Element not found")
    else:
        output_label.config(text="Markdown Generated")
        pyperclip.copy(markdown_text)#複製Markdown到剪貼簿
    #driver.quit()

if __name__ == '__main__':
    root=tk.Tk()
    root.title("LeetCode Markdown Generator")
    root.geometry('400x400')
    
    #URL標籤
    url_label=tk.Label(root,text="URL:")
    url_label.pack()
    
    #URL輸入框
    url_entry=tk.Entry(root)
    url_entry.pack()

    #生成Markdown按鈕
    save_button=tk.Button(root,text="Generate Markdown",command=generate_markdown)#生成Markdown按鈕
    save_button.pack()

    #輸出標籤
    output_label=tk.Label(root,text="")#輸出標籤
    output_label.pack()

    #退出按鈕
    quit_button=tk.Button(root,text="Quit",command=Quit)#退出按鈕
    quit_button.pack()

    root.mainloop()
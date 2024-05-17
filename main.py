import tkinter as tk
from tkinter import filedialog
from get_images_url import get_images_url
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_var.set(folder_path)
    else:
        folder_path_var.set("No folder selected.")

# 创建主窗口
root = tk.Tk()
root.title("Folder Selector")
root.geometry("500x300")

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=20)
# 创建显示文件夹路径的变量
folder_path_var = tk.StringVar()
folder_path_var.set("No folder selected.")

# 创建选择文件夹按钮
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

# 创建显示文件夹路径的标签
folder_label = tk.Label(root, textvariable=folder_path_var, wraplength=400)
folder_label.pack(pady=20)

download_button = tk.Button(root, text="Download", command=lambda: get_images_url(url_entry.get(), folder_path_var.get()))
download_button.pack(pady=20)

# 启动GUI主循环
root.mainloop()

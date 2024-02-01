import os
import shutil

current_location = os.getcwd()

items = os.listdir(current_location)

for item in items:
    if item.endswith(".pdf"):
        shutil.move(item, r"C:\Users\Admin\Desktop\pdfs")
    elif item.endswith(".exe"):
        shutil.move(item, r"C:\Users\Admin\Desktop\exes")
    elif item.endswith(".docx"):
        shutil.move(item, r"C:\Users\Admin\Desktop\docx")
    elif item.endswith(".xlsx"):
        shutil.move(item, r"C:\Users\Admin\Desktop\xlsxs")
    elif item.endswith(".jpeg") or item.endswith(".jpg") or item.endswith(".png"):
        shutil.move(item, r"C:\Users\Admin\Desktop\Images")
    elif item.endswith(".txt"):
        shutil.move(item, r"C:\Users\Admin\Desktop\txts")
    else:
        shutil.move(item, r"C:\Users\Admin\Desktop\miscs")
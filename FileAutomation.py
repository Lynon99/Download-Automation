from importlib.resources import path
from operator import truediv
import os, shutil
print("Welcome to the File Automation program. \n Remember to use the correct directory name. \n EX: C:/Users/User1/Downloads")
source_dir = input("Where would you like to automate your files?")
dest_dir_pdf = input("Where would you like to move your PDFs?")
dest_dir_image = input("Where would you like to move your Images?")
dest_dir_documents = input("Where would you like to move your Documents?")
dest_dir_video = input("Where would you like to move your Videos?")
dest_dir_archive = input("Where would you like to move your Archives?")
print("You can close the program or let it run in the background to automatically move your files. \n Thanks for using File Automator!")
while True:
        
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        if os.path.join(source_dir, file_name).endswith('.pdf'):
            shutil.move(os.path.join(source_dir, file_name), dest_dir_pdf)
        if os.path.join(source_dir, file_name).endswith('.docx'):
            shutil.move(os.path.join(source_dir, file_name), dest_dir_documents) 
        if os.path.join(source_dir, file_name).endswith(".jpg") or os.path.join(source_dir, file_name).endswith(".png"):
            shutil.move(os.path.join(source_dir, file_name), dest_dir_image)
        if os.path.join(source_dir, file_name).endswith(".mp4"):
            shutil.move(os.path.join(source_dir, file_name), dest_dir_video)
        if os.path.join(source_dir, file_name).endswith(".zip"):
            shutil.move(os.path.join(source_dir, file_name), dest_dir_archive)    
            
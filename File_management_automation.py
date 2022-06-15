from importlib.resources import path
from operator import truediv
import os, shutil

source_dir = "C:/Users/lynonsmith/Downloads"
dest_dir_pdf = "C:/Users/lynonsmith/Downloads/PDF"
dest_dir_image = "C:/Users//lynonsmith//pictures"
dest_dir_documents = "C:/Users/lynonsmith/downloads/Docs"
dest_dir_video = "C:/Users/lynonsmith/videos"
dest_dir_archive = "C:/Users/lynonsmith/downloads/Archive"

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
            
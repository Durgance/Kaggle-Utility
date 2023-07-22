import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import os
import sys

api = KaggleApi()
api.authenticate()
compition_name = input("Please Input the name of Compition : ")
folder_name = input("Input location to save data : ")

b = """
⠄⠄⠄⠄⠄⠄⣠⣤⣶⣶⣿⣶⣶⣤⣀⠄⣀⣤⣴⣶⣶⣶⣦⣀⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣤⣿⠡⢟⡿⠿⣛⣛⣛⠿⢿⡆⢻⣿⣿⣿⣿⣯⣃⣸⣧⡀⠄⠄⠄⠄
⠄⠄⢀⣾⣿⣿⣋⣵⣾⣿⣿⣿⣿⣿⣷⣶⡄⣩⣴⣶⣶⣶⣶⣶⣭⣉⣀⠄⠄⠄
⠄⢀⣿⡟⣻⣿⣿⣿⣿⠟⢋⣭⣴⣶⣶⣶⣦⣮⡙⠟⢛⣭⣭⣶⣶⣶⣮⣭⣄⠄
⣴⣸⣿⠑⣛⣿⠟⢩⣶⣿⣿⣿⣿⣿⡏⡋⠉⣿⣿⡌⣿⣿⣿⣿⣿⠋⡋⠛⣿⣧
⢿⣿⣿⣿⣿⣿⣶⣶⣭⣝⡻⠿⣿⣿⣷⣧⣵⠿⢟⡑⠿⠿⠿⠿⠿⠶⠭⠶⠟⠃
⣬⣿⣿⣿⣿⣿⣿⣿⣷⣬⣙⣛⣒⠠⢤⣤⡔⢚⣛⣴⣿⣿⣿⣿⣿⣿⣿⡿⠛⠄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣋⣱⣾⣿⣿⣿⣎⡙⢛⣋⣉⣉⣅⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣭⡝⢿⣿⣿⣿⣦⠄⠄
⣿⣿⣿⣿⣿⣿⠿⣛⣩⣭⣭⣭⣛⣛⠿⠿⢿⣿⣿⡏⣾⣿⡇⢸⣿⡿⠿⢛⣃⠄
⣿⣿⣿⣿⣿⡏⢾⣿⣯⣭⣍⣛⣛⣛⡻⠶⠶⣮⣭⢡⣿⣿⢇⣭⣵⣶⠾⠿⠋⠄
⣿⣿⣿⣿⣟⢿⣦⣤⣭⣭⣭⣝⣛⡻⠿⠿⠿⠶⠶⢸⣿⣿⢠⣤⣤⣶⠾⠛⠄⠄
⠿⢿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣾⣿⡿⠰⠖⠄⠄⠄⠄⠄⠄
⣭⣕⠒⠲⣭⣭⣝⣛⠛⠛⠛⠛⠛⠛⠛⢛⣛⣭⠄⣿⡟⢣⣴⣾⠟⢂⣤⡀⠄⠄
⣿⣿⣿⣿⣶⣶⣮⣭⣭⣭⣍⣛⣛⣉⣭⣭⣭⣶⢸⣿⣿⣿⣯⣴⠞⣛⣭⣶⣷⠄"""

print(b)

api.competition_download_files(compition_name, folder_name)
ziped_file = folder_name+"\\"+compition_name+".zip"
with zipfile.ZipFile(ziped_file,'r') as zipref:
    zipref.extractall("./"+folder_name)
os.remove(ziped_file)
saitama = """

⠀⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀
⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷
⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀DONE⠀⡇
⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇
⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼
⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀
⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀⠀
"""
print(saitama)
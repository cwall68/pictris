import os

datei = __file__
print("___")
print(datei)
verz = os.getcwd()
print("___")
print(verz)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f'BASE_DIR: {BASE_DIR}')

pic_dir = os.path.join(BASE_DIR,"best of puzzles")
print(f'Bilder in: {pic_dir}')
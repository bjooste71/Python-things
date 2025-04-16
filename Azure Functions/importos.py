import os

for folder,subfolder,files in os.walk('.'):
    print(folder,subfolder,files)


os.scandir()
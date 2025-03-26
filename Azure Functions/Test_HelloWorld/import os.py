import os
import send2trash
z = os.getcwd()

f = open('testtext.txt','w+')

f.write(f'{z}')

os.listdir()

send2trash.send2trash('testtext.txt')

for folder, subfolders, files in os.walk(z):
    print(f"Current looking at {folder}")
    print("\n")
    for subfold in subfolders:
        print(f'\tSubfolder: {subfold}')
    for f in files:
        print(f'\t{f}')
    print('\n')
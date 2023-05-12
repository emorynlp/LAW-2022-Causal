import zipfile
import os

directory = "/Users/angelacao1/Desktop/annotation"



for x in os.listdir(directory):
 directory2 = os.path.join(directory, x)

for y in os.listdir(directory2):
    zip_filename = os.path.join(directory2, y)

with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(directory2)

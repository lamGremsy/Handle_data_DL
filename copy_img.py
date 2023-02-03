import os
from pathlib import Path
import shutil
from PIL import Image
from tqdm import tqdm

dir = Path('/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/download')
dir_2 = Path('/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/boat_images')
# arr = os.listdir(dir/'download_1')
# print(arr)
for i in range(29,126,1):
    arr = os.listdir(dir/f'download_{i}')
    for file_name in arr:
        # print(file_name)
        source = dir/f'download_{i}'/Path(file_name)
        destination = dir_2 /Path(file_name)
        # copy only files
        if os.path.isfile(source):
            shutil.copyfile(source, destination)
            print(f'copied download_{i}', file_name)
        # os.rmdir(dir/'sequences'/f)
import os
from pathlib import Path
from PIL import Image
from tqdm import tqdm
import numpy as np
import argparse
import shutil

parser_arg = argparse.ArgumentParser()
# parser_arg.add_argument('--pathyolo', type=str, default='/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/boat_data', help='path')
parser_arg.add_argument('--pathyolo', type=str, default='/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/data_boat_final/train', help='path')
path = parser_arg.parse_known_args()[0]
dir = Path(path.pathyolo)

# Kiểm tra và xóa các file images không có lables
def missing_images(dir):
    img_name= os.listdir(dir / 'images')
    label_name= os.listdir(dir / 'labels')
    print(len(img_name))
    print(len(label_name))
    img_cus=[]
    label_cus=[]
    for i in img_name:
        name_1=str(i).split('.jpg')
        img_cus.append(str(f"{name_1[0]}"))
    for k in label_name:
        name_2=str(k).split('.txt')
        # print(name_2[0])
        for p1 in img_cus:
            if name_2[0] == p1:
                # img_cus.remove(p1)

                label_cus.append(str(f"{name_2[0]}"))
    print(len(img_cus))
    print(len(label_cus))
    for file in label_cus:
        filename = file + '.jpg'
        source = dir / 'images' / filename
        destination = dir / 'images_cus' / filename
        # shutil.copyfile(source, destination)


# Kiểm tra và xóa các file labels không có images
def missing_labels(dir):
    img_name= os.listdir(dir / 'images')
    label_name= os.listdir(dir / 'labels')
    print(len(img_name))
    print(len(label_name))
    img_cus=[]
    label_cus=[]
    for i in label_name:
        name_1=str(i).split('.txt')
        img_cus.append(str(f"{name_1[0]}"))
    for k in img_name:
        name_2=str(k).split('.jpg')
        # print(name_2[0])
        for p1 in img_cus:
            if name_2[0] == p1:
                # img_cus.remove(p1)

                label_cus.append(str(f"{name_2[0]}"))
    print(len(img_cus))
    print(len(label_cus))
    for file in label_cus:
        filename = file + '.txt'
        source = dir / 'labels' / filename
        destination = dir / 'labels_cus' / filename
        # shutil.copyfile(source, destination)
    
# missing_images(dir)
missing_labels(dir)
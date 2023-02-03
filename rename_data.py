import os
from pathlib import Path
from PIL import Image
from tqdm import tqdm
import numpy as np
import argparse
import shutil

parser_arg = argparse.ArgumentParser()
parser_arg.add_argument('--pathyolo', type=str, default='/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/data_boat_final/val', help='path')
path = parser_arg.parse_known_args()[0]
dir = Path(path.pathyolo)

def rename_data(dir):
    img_name= os.listdir(dir / 'images')
    label_name= os.listdir(dir / 'labels')
    print(len(img_name))
    print(len(label_name))
    img_cus=[]
    label_cus=[]
    count = 1
    (dir / 'images_cus').mkdir(parents=True, exist_ok=True)
    (dir / 'labels_cus').mkdir(parents=True, exist_ok=True)
    for i in label_name:
        name_1=str(i).split('.txt')
        if name_1[0] != 'classes':
        
            # label_cus.append(str(f"{name_1[0]}"))
            rename = f'boat_{count}'
            
            img = str(name_1[0]) + '.jpg'
            img_new = rename + '.jpg'
            label = str(name_1[0]) + '.txt'
            label_new = rename + '.txt'
            source_img = dir / 'images' / img
            destination_img = dir / 'images_cus' / img_new
            source_label = dir / 'labels' / label
            destination_label = dir / 'labels_cus' / label_new
            print('Copy ',str(name_1[0]), '----------> ', rename)
            shutil.copyfile(source_img, destination_img)
            shutil.copyfile(source_label, destination_label)

            count=count+1



    # for k in label_name:
    #     name_2=str(k).split('.txt')
    #     # print(name_2[0])
    #     for p1 in img_cus:
    #         if name_2[0] == p1:
    #             # img_cus.remove(p1)

    #             label_cus.append(str(f"{name_2[0]}"))
    # print(len(img_cus))
    # print(len(label_cus))
    # for file in label_cus:
    #     filename = file + '.jpg'
    #     source = dir / 'images' / filename
    #     destination = dir / 'images_cus' / filename
    #     # shutil.copyfile(source, destination)

rename_data(dir)
import os
from pathlib import Path
import shutil
from PIL import Image
from tqdm import tqdm

# dir = Path('/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/data-DET/train')
# dir = Path('/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/visdrone/Task_1_Object_Detection_in_Images/VisDrone2019-DET-train')
# dir = Path('/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/Roboflow/test project.v1-amdata.yolov5pytorch/train')
dir = Path('/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/data_final/boat_data_final')

labels_count = [0,0,0,0,0,0,0,0,0,0,0]

def print_count_labels_visdrone(count):
    print("_____________________________")
    print("|| labels         | count")
    print("=============================")
    print("|| pedestrian     |",count[0])
    print("|| people         |",count[1])
    print("|| bicycle        |",count[2])
    print("|| car            |",count[3])
    print("|| van            |",count[4])
    print("|| truck          |",count[5])
    print("|| tricycle       |",count[6])
    print("|| awning-tricycle|",count[7])
    print("|| bus            |",count[8])
    print("|| motor          |",count[9])
    print("|| boat           |",count[10])
    print("_____________________________")


pbar = tqdm((dir / 'custom_label').glob('*.txt'), desc=f'Converting {dir}')
# pbar = tqdm((dir / 'labels').glob('*.txt'), desc=f'Converting {dir}')
for f in pbar:
    g=str(f.name).split('.txt')
    with open(f, 'r') as file:  # read annotation.txt
        for row in [x.split(' ') for x in file.read().strip().splitlines()]:
            if row[0]=='0':
                labels_count[0]=labels_count[0]+1
            if row[0]=='1':
                labels_count[1]=labels_count[1]+1
            if row[0]=='2':
                labels_count[2]=labels_count[2]+1
            if row[0]=='3':
                labels_count[3]=labels_count[3]+1
            if row[0]=='4':
                labels_count[4]=labels_count[4]+1
            if row[0]=='5':
                labels_count[5]=labels_count[5]+1
            if row[0]=='6':
                labels_count[6]=labels_count[6]+1
            if row[0]=='7':
                labels_count[7]=labels_count[7]+1
            if row[0]=='8':
                labels_count[8]=labels_count[8]+1
            if row[0]=='9':
                labels_count[9]=labels_count[9]+1
            if row[0]=='10':
                labels_count[10]=labels_count[10]+1

print_count_labels_visdrone(labels_count)
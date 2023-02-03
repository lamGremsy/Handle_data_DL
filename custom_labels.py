import os
from pathlib import Path
from PIL import Image
from tqdm import tqdm
import numpy as np
import argparse

parser_arg = argparse.ArgumentParser()
# parser_arg.add_argument('--pathyolo', type=str, default='/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/Roboflow/databoat_3/train', help='path')
parser_arg.add_argument('--pathyolo', type=str, default='/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/dataset/data_final/boat_data_final', help='path')
path = parser_arg.parse_known_args()[0]
dir = Path(path.pathyolo)

def custom_label(dir):
    (dir / 'custom_label').mkdir(parents=True, exist_ok=True)
    pbar = tqdm((dir / 'labels').glob('*.txt'), desc=f'Converting {dir}')
    for f in pbar:
        g=str(f.name).split('.txt')
        lines = []
        
        with open(f, 'r') as file:
            for row in [x.split(' ') for x in file.read().strip().splitlines()]:
                if row[0]=='1' or row[0]=='0' or row[0]=='2':
                    if row[0]=='0':
                        row[0]=10
                    # if row[0]=='2':
                    #     row[0]=0
                    for r in row:
                        lines.append(f"{r} ")
                    lines.append(f"\n")
                with open(dir / 'custom_label'/ Path(str(g[0])+'.txt') , 'w') as fl:
                    fl.writelines(lines)


custom_label(dir)
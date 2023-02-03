import os
from pathlib import Path
import shutil
from PIL import Image
from tqdm import tqdm
dir = Path('/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/data-DET/train')
def visdrone2yolo(dir):
      from PIL import Image
      from tqdm import tqdm
      def convert_box(size, box):
          # Convert VisDrone box to YOLO xywh box
          dw = 1. / size[0]
          dh = 1. / size[1]
          return (box[0] + box[2] / 2) * dw, (box[1] + box[3] / 2) * dh, box[2] * dw, box[3] * dh
      (dir / 'labels_pre').mkdir(parents=True, exist_ok=True)  # make labels directory
      pbar = tqdm((dir / 'annotations').glob('*.txt'), desc=f'Converting {dir}')
      for f in pbar:
          img_size = Image.open((dir / 'images' / f.name).with_suffix('.jpg')).size
          lines = []
          with open(f, 'r') as file:  # read annotation.txt
              for row in [x.split(',') for x in file.read().strip().splitlines()]:
                  if row[4] == '0':  # VisDrone 'ignored regions' class 0
                      continue
                  cls = int(row[5]) - 1
                  box = convert_box(img_size, tuple(map(int, row[:4])))
                  lines.append(f"{cls} {' '.join(f'{x:.6f}' for x in box)}\n")
                  with open(str(f).replace(os.sep + 'annotations' + os.sep, os.sep + 'labels_pre' + os.sep), 'w') as fl:
                      fl.writelines(lines)  # write label.txt
                        
for d in ['VisDrone2019-DET-train']:
    visdrone2yolo(dir / d) 
    # custom_label(dir / d) # custom label 
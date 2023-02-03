import os
from pathlib import Path
import shutil
from PIL import Image
from tqdm import tqdm
dir = Path('/media/lam/HDD/Gremsy/Source_Code/7_Object_Detection/visdrone/Task 4: Multi-Object Tracking/convert')
def visdrone2yolo(dir):

      def convert_box(size, box):
          # Convert VisDrone box to YOLO xywh box
          dw = 1. / size[0]
          dh = 1. / size[1]
          return (box[0] + box[2] / 2) * dw, (box[1] + box[3] / 2) * dh, box[2] * dw, box[3] * dh

      (dir / 'labels').mkdir(parents=True, exist_ok=True)  # make labels directory
      pbar = tqdm((dir / 'annotations').glob('*.txt'), desc=f'Converting {dir}')
      for f in pbar:
        g=str(f.name).split('.')
        arr = os.listdir(dir/'sequences'/g[0])
        for img in arr:
          img_size = Image.open((dir / 'sequences' / g[0] / img).with_suffix('.jpg')).size
          os.rename(dir / 'sequences' / g[0] / img,dir / 'sequences' / g[0] / Path(str( g[0]+'_'+ (str(img).split('.')[0]) +'.jpg')))
          lines = []
          with open(f, 'r') as file:  # read annotation.txt
              for row in [x.split(',') for x in file.read().strip().splitlines()]:
                if int(row[0])==int((str(img).split('.'))[0]):
                    if row[6] == '0':  # VisDrone 'ignored regions' class 0
                        continue
                    cls = int(row[7]  ) - 1
                    box = convert_box(img_size, tuple(map(int, row[2:6])))
                    lines.append(f"{cls} {' '.join(f'{x:.6f}' for x in box)}\n")
                    with open(dir / 'labels'/Path(str( g[0]+'_'+ (str(img).split('.')[0])+'.txt')) , 'w') as fl:
                        fl.writelines(lines)  # write label.txt

def movefile(dir):
    arr = os.listdir(dir/'sequences')
    for f in arr: 
        for file_name in os.listdir(dir/'sequences'/f):
        # construct full file path
            source = dir/'sequences'/f /Path(file_name)
            destination = dir/'sequences' /Path(file_name)
            # copy only files
            if os.path.isfile(source):
                shutil.move(source, destination)
                print('copied', file_name)
        os.rmdir(dir/'sequences'/f)
                        
for d in ['VisDrone2019-MOT-val']:
        visdrone2yolo(dir / d)  # convert VisDrone annotations to YOLO labels
        # movefile(dir/d)
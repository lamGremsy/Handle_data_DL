# <span style= 'color:#00BFFF'>Handle Data Deep Learning (Object Detection)</span> 

## <span style= 'color:gold'>Create Labels</span>
```bash
$ git clone https://github.com/heartexlabs/labelImg.git
$ python3 labelImg/labelImg.py
```


## <span style= 'color:gold'>Information Python File</span>

### <span style= 'color:khaki'>Convert labels VisDrone to YOLOv5 ---> VisdroneDET_2_Yolo.py / VisdroneMOT_2_Yolo.py</span>
```
Chuyển đổi định dạng file label.txt của Visdrone thành dạng label.txt của YOLOv5
+ VisdroneDET_2_Yolo.py ---> Chuyển đổi định dạng của tập data Visdrone DET (Object Detection in Images)
+ VisdroneMOT_2_Yolo.py ---> Chuyển đổi định dạng của tập data Visdrone MOT (Multi-Object Tracking)
```

### <span style= 'color:khaki'>Download Image From Wedsite ---> download_img.py</span>
```
Download nhanh tất cả hình có trong đường dẫn URL
ex: url = 'https://www.dreamstime.com/photos-images/drone-sea-boat.html' 
```

### <span style= 'color:khaki'>Check Number of Labels in Dataset ---> check_number_labels.py</span>
```
Kiểm tra số  lượng đã đánh được của từng label trong tập dataset
```

### <span style= 'color:khaki'>Missing Images File or Labels File ---> missing_labels_imgs.py</span>
```
Kiểm tra và xóa các file images không có labels và các file labels khồn có images
```

## <span style= 'color:gold'>Link </span>

<!-- ### <span style= 'color:khaki'>Dataset VisDrone: </span> -->
### [Dataset VisDrone](https://github.com/VisDrone/VisDrone-Dataset)
### [Data Boat Download](https://www.dreamstime.com/photos-images/drone-sea-boat.html)
### [Convert Labels YOLOv5 to PascalVOC](https://github.com/carolinepacheco/convert-yolo-to-pascalvoc/blob/master/yolo_to_voc.py)
### []()
### []()
### []()
### []()
### []()
### []()
### []()
### []()
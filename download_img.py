import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

# The path of the images you want to download
url = 'https://www.dreamstime.com/photos-images/drone-sea-boat.html?pg='
count_page = 2


def download_img(url,i):
    is_download = False
    while 1:
        print("------------------------- PAGE ",i," -------------------------","\n")
        pageTarget = url + str(i)
        page = requests.get(pageTarget)
        soup = BeautifulSoup(page.content, 'html.parser')
        wrapper = soup.find('body')
        # print(page,"\n")
        # print(soup.prettify(),"\n")
        # print(wrapper,"\n")

        images = wrapper.find_all("img",{"data-src":True})
        # print(images,"\n")
        if images != []:
            print('DOWLOADING....\n')
        for image in images:
            imgData = image['data-src']
            # print(imgData,"\n")
            if("dat:image" not in imgData):
                print(imgData)
                if(imgData):
                    pathdir=Path('/home/lam/WIN/Gremsy/Source_Code/7_Object_Detection/Code_python/download/download_'+str(i))
                    (pathdir).mkdir(parents=True, exist_ok=True)
                    downloadPath = './download/download_'+str(i)+'/'
                    filename = imgData.split('/')[-1]

                    response = requests.get(imgData)

                    file = open(downloadPath + filename, "wb")
                    file.write(response.content)
                    file.close()
                    is_download = True
        if is_download:
            print('\nDONE DOWLOAD....\n')
            break

for i in range(2,126,1):
    download_img(url,i)
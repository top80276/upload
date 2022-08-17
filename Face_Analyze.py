from cgitb import reset
from locale import resetlocale
from platform import release
from deepface import DeepFace
import matplotlib.pyplot as plt
from PIL import Image

import sys 
import json

import os


def main():
    # 檔案路徑
    # 取的img內最新建立的照片
    dir = r"C:\Users\Student\Downloads\upload-main\public\img"
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
    if not os.path.isdir(dir + "\\" + fn) else 0)
    file = os.path.join(dir, file_lists[-1])
    img1_path = file
    # 偵測臉部
    img1 = DeepFace.detectFace(img1_path)
    # 分析照片
        # Obj =DeepFace.analyze(img_path = img1_path)
    # 單獨拉出項目
    demography = DeepFace.analyze(img1_path, ['age', 'gender', 'race', 'emotion'], prog_bar = False)


        # Obj ={"Age": demography["age"], "Gender":demography["dominant_gender"], "Race":demography["dominant_race"], "Emotion":demography["dominant_emotion"]}



    print("Age: ", demography["age"])
    # 原本為demography["dominant_gender"])，但我的執行結果沒有這項，改為demography["gender"]
    print("Gender: ", demography["gender"])
    print("Race: ", demography["dominant_race"])
    print("Emotion: ", demography["dominant_emotion"])

    # raw_img1 = Image.open(img1_path)
    # plt.imshow(raw_img1)
    # plt.show()

    # print(demography)



    # json = json.dumps(demography)

    # print(str(json))

    # sys.stdout.flush()

    # return Obj



if __name__ == '__main__':
    data = main()
    print(data)
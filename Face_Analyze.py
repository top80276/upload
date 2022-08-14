from cgitb import reset
from locale import resetlocale
from platform import release
from deepface import DeepFace
import matplotlib.pyplot as plt
from PIL import Image

import sys 
import json


def main():
    # 檔案路徑
    img1_path = './public/img/001.jpg'
    # 偵測臉部
    img1 = DeepFace.detectFace(img1_path)
    # 分析照片
        # Obj =DeepFace.analyze(img_path = img1_path)
    # 單獨拉出項目
    demography = DeepFace.analyze(img1_path, ['age', 'gender', 'race', 'emotion'], prog_bar = False)


        # Obj ={"Age": demography["age"], "Gender":demography["dominant_gender"], "Race":demography["dominant_race"], "Emotion":demography["dominant_emotion"]}



    print("Age: ", demography["age"])
    print("Gender: ", demography["dominant_gender"])
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
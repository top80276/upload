from locale import resetlocale
from deepface import DeepFace
import matplotlib.pyplot as plt
from PIL import Image

import sys 
import json

img1_path = './public/img/001.jpg'

img1 = DeepFace.detectFace(img1_path)

Obj =DeepFace.analyze(img_path = img1_path)

demography = DeepFace.analyze(img1_path, ['age', 'gender', 'race', 'emotion'])



# print("Age: ", demography["age"])
# print("Gender: ", demography["dominant_gender"])
# print("Race: ", demography["dominant_race"])
# print("Emotion: ", demography["dominant_emotion"])

# raw_img1 = Image.open(img1_path)
# plt.imshow(raw_img1)
# plt.show()

print(demography)



# json = json.dumps(demography)

# print(str(json))

sys.stdout.flush()
from typing import Counter
from mtcnn import MTCNN
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.patches import Rectangle
from pprint import pprint

def mtmain():
   # 照片路徑
   img1_path = './public/img/mtcnn1.jpg'
   img1 = Image.open(img1_path)


   # MTCMM偵測人臉
   img = cv2.cvtColor(cv2.imread(img1_path), cv2.COLOR_BGR2RGB)
   detector = MTCNN()

   detections = detector.detect_faces(img)

   # 計算每個人臉的embeddings
   # embeddings = []
   # for detection in detections:
   #    confidence = detection["confidence"]
   #    if confidence > 0.90:
   #       x, y, w, h = detection["box"]
   #       detected_face = img[int(y):int(y+h), int(x):int(x+w)]
         
   #       embedding = DeepFace.represent(detected_face, model_name = 'Facenet', enforce_detection = False)
   #       embeddings.append(embedding)
   # print(embeddings[0])


   # 分析每個人臉的結果
   objs = []
   for detection in detections:
      confidence = detection["confidence"]
      if confidence > 0.90:
         x, y, w, h = detection["box"]
         detected_face = img[int(y):int(y+h), int(x):int(x+w)]
         
         obj = DeepFace.analyze(detected_face, enforce_detection = False)
         objs.append(obj)



   # pprint(objs)


   
   # 偵測畫box function
   def draw_image_with_boxes(img1_path, result_list):
      # 讀取圖片路徑
      data = plt.imread(img1_path)
      # 畫圖
      plt.imshow(data)

      ax = plt.gca()
      # 畫box
      for result in result_list:
         # 取得座標和寬高
         x, y, width, height = result['box']
         # 設定box內容
         rect = Rectangle((x, y), width, height, fill=False, color='green')
         # 畫 box
         ax.add_patch(rect)
      # show the plot
      # plt.show()
   
   pixels = plt.imread(img1_path)
   detector = MTCNN()
   # 偵測人臉
   faces = detector.detect_faces(pixels)
   # 將box 繪製在照片上
   draw_image_with_boxes(img1_path, faces)
   # 存圖檔
   plt.savefig('./public/img/mtcnn2.jpg')



   # 情緒列表
   emotion_key = 'dominant_emotion'
   emotion_output = dict(Counter(sub[emotion_key] for sub in objs))
   print(emotion_output)

   # 年齡列表
   age_key = 'age'
   age_output = dict(Counter(sub[age_key] for sub in objs))
   print(age_output)

   # 性別列表
   gender_key = 'gender'
   gender_output = dict(Counter(sub[gender_key] for sub in objs))
   print(gender_output)

   # 群眾滿意度
   all = gender_output['Man']+gender_output['Woman']
   happy =(emotion_output['happy']/all)*100
   print(f'happiness:{happy}%')

if __name__ == '__main__':
    data = mtmain()
    print(data)


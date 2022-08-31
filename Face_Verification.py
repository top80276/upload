from deepface import DeepFace
import matplotlib.pyplot as plt
from PIL import Image
import os

def compare():
    # 兩張照片的路徑
    img1_path = './public/img/ver0.jpg'
    img2_path = './public/img/ver1.jpg'

    # 兩張人臉照片
    img1 = DeepFace.detectFace(img1_path)
    img2 = DeepFace.detectFace(img2_path)

    # 兩張原始照片
    raw_img1 = Image.open(img1_path)
    raw_img2 = Image.open(img2_path)

    plt.figure(figsize=(12, 8))
    plt.subplot(221)
    plt.imshow(raw_img1)

    plt.subplot(222)
    plt.imshow(raw_img2)

    plt.subplot(223)
    plt.imshow(img1)

    plt.subplot(224)
    plt.imshow(img2)
    plt.savefig('./public/img/ver3.jpg')

    # model_name = 'Facenet'
    # resp = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name = model_name)
    # print('model',resp["model"])
    # print("verified:",resp["verified"])
    # print("distance",resp["distance"])

    model_name = 'VGG-Face'
    resp = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name = model_name)
    print('model',resp["model"])
    print("distance",resp["distance"])
    print("threshold:",resp["threshold"])
    print("verified:",resp["verified"])
    # print(resp)

    # model_name = 'ArcFace'
    # resp = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name = model_name)
    # print('model:',resp["model"])
    # print("verified:",resp["verified"])
    # print("distance",resp["distance"])

#distance越小 相似度越高


#threshold:With a distance threshold of 0.6, the dlib model achieved an accuracy of 99.38% on the standard LFW face recognition benchmark,which places it among the best algorithms for face recognition.




if __name__ == '__main__':
    data = compare()
    print(data)


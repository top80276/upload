import re
from datetime import datetime
import time as ti
import cv2
from deepface import DeepFace
from csv import writer

#-*- coding: utf-8 -*-


# 呼叫電腦攝像頭檢測人臉並截圖

def CatchPICFromVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)

    # 視訊來源，可以來自一段已存好的視訊，也可以直接來自USB攝像頭
    cap = cv2.VideoCapture(camera_idx)

    # 告訴OpenCV使用人臉識別分類器
    classfier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

    # 識別出人臉後要畫的邊框的顏色，RGB格式
    color = (0, 255, 0)

    value = 0
    while cap.isOpened():
        ok, frame = cap.read() # 讀取一幀資料
        if not ok:
            break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #將當前楨影象轉換成灰度影象

        # 人臉檢測，1.2和2分別為圖片縮放比例和需要檢測的有效點數
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0:          #大於0則檢測到人臉
            for faceRect in faceRects:  #單獨框出每一張人臉
                x, y, w, h = faceRect
                

                # 避免太快暫時停一秒
                # ti.sleep(1)

                # 將當前幀儲存為圖片
                img_name = "webcam001.jpg" 

                # print(img_name)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])


                # 畫出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                # 顯示當前捕捉到人臉圖片+框
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,'face' ,(x + 30, y + 30), font, 1, (255,0,255),4)


                if value == 10:   #跑10個迴圈後啟動一次
                    # 打卡登入系統
                    # 比對的照片庫路徑
                    # 路徑放 ./testimg/(英文人名)  英文人名資料夾放對應照片 資料夾回產生representations_facenet.pkl 存照片embedding
                    db_path ="./testimg"
                    df = DeepFace.find(
                    img_path = "webcam001.jpg", 
                    db_path = db_path,
                    model_name = 'Facenet',
                    enforce_detection=False)
                    # print("================================")
                    # print(df.head(1))
                    # print("================================")
                    # print(df['identity'])
                    # print("================================")                
                    if len(df) > 0:  # 如果有找到對應照片
                        # 找出對應照片的人名
                        emp =str(df.head(1)['identity'])
                        empno = re.findall(r'[^\\]+(?=/)',emp)[-1]
                        # print(empno)
                        # 現在時間
                        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')                     
                        print(f'welcome {empno} login!')
                        print(f'login time:{time}')


                        # 將名字和時間存LIST
                        list_data=[empno,time]                       

                        # 將LIST資料存到.cvs
                        time2 = datetime.now().strftime('%Y_%m_%d')
                        with open('test.csv', 'a', newline='') as f_object:  
                            writer_object = writer(f_object)
                            writer_object.writerow(list_data)  
                            f_object.close()

                    else:
                        # 如果沒找到對應照片
                        print("抱歉，登入失敗!!") 

                    value = 0
                value += 1
                # print(value)



        # 顯示影象
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        # 按按鍵q離開視訊
        if c & 0xFF == ord('q'):
            break

    # 解除攝像頭和視窗
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    CatchPICFromVideo("get face", 0)




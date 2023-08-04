from DataBase import *
import time
import cv2
from deepface import DeepFace
import datetime


duygular=Duygular()

print("""1.Duygulari Göster\n2.Duygulari Veritabanına Kaydet""")

duygu_listesi=[]

while True:
    islem=input("Yapacağiniz işlemi seçiniz : ")

    if(islem=='q'):
        print("Çikiş Yapiliyor...")
        break

    elif(islem=="1"):
        duygular.duygu_goster()
    elif(islem=="2"):
        cascade=cv2.CascadeClassifier('cascade.xml')
        cap=cv2.VideoCapture(1)
        musteri_ismi=input("Müşteri İsmi : ")
        calisan_ismi=input("Çalişan İsmi :")
        urun=input("Ürün İsmi :")
        time_now=datetime.datetime.now()
        print("Kamera Açiliyor...")
        time.sleep(1)

        if not cap.isOpened():
            cap=cv2.VideoCapture(0)
        if not cap.isOpened():
            raise IOError('Cannot open Webcam')

        while True:
            ret,frame=cap.read()
            frame=cv2.flip(frame,1)
            result=DeepFace.analyze(frame,actions=['emotion'])

            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            emo=cascade.detectMultiScale(gray,1.1,4)


            for (x,y,w,h) in emo:
                cv2.rectangle(frame,(x,y),(x+w,y+w),(79,79,79),1)
            
            font=cv2.FONT_HERSHEY_COMPLEX_SMALL

            cv2.putText(frame,result['dominant_emotion'],(120,50),font,3,(245,245,220),2)

            cv2.imshow("Video",frame)


            duygu_listesi.append(result['dominant_emotion'])
            emotion_count=max(set(duygu_listesi),key=duygu_listesi.count)
            

            if emotion_count =='sad' or emotion_count=='angry' or emotion_count=='disgust' or emotion_count=='fear':
                emotion_count='Beğenmedi'
            else:
                emotion_count='Beğendi'
            
            ruh_hali=emotion_count


          

            if cv2.waitKey(2) & 0xFF == ord('q'):
                yeni_duygu=Duygu(ruh_hali,musteri_ismi,calisan_ismi,urun,time_now)
                print("Ekleniyor..")
                time.sleep(1) 
                duygular.ekle(yeni_duygu)
                print("Eklendi!")
                break
        
        
        print(ruh_hali,musteri_ismi,calisan_ismi,urun,time_now)
                    
        cap.release()
        cv2.destroyAllWindows()




        
        
    
    



    
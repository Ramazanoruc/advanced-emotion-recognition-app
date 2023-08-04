from typing_extensions import Self
from deepface import DeepFace
import matplotlib.pyplot as plt
import sqlite3
import mysql.connector



class Duygu():

    def __init__(self,ruh_hali,musteri_ismi,calisan_ismi,urun,time_now):
        self.ruh_hali=ruh_hali
        self.musteri_ismi=musteri_ismi
        self.calisan_ismi=calisan_ismi
        self.urun=urun
        self.time_now=time_now

    def __str__(self):
        return "Emotional State : {}\nClient : {}\nEmployee : {}\nProduct : {}\nTime : {}".format(self.ruh_hali,self.musteri_ismi,self.calisan_ismi,self.urun,self.time_now)


class Duygular():
    def __init__(self):
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        self.baglanti= mysql.connector.connect(user='metapiens_ai', password='+1FR_305^978',
                              host='80.253.246.193',
                              database='metapiens_ai')
        self.cursor=self.baglanti.cursor()
    def baglantiyikes(self):
        self.baglanti.close()

    def duygu_goster(self):
        sorgu="SELECT * FROM Duygular "
        self.cursor.execute(sorgu)

        duygular2=self.cursor.fetchall()
        j=1
        for i in duygular2:
            duygu=Duygu(i[0],i[1],i[2],i[3])
            print("----------{}.DATA----------".format(j))
            j+=1
            print(duygu)
    
    def ekle(self,duygu):
        sorgu = """INSERT INTO sentiment_analysis (Mood,CustomerName,EmployeeName,Product,Date) VALUES (%s,%s,%s,%s,%s)"""
        self.cursor.execute (sorgu,(duygu.ruh_hali,duygu.musteri_ismi,duygu.calisan_ismi,duygu.urun,duygu.time_now))
        self.baglanti.commit()
        #self.cursor.execute(sorgu,(duygu.ruh_hali))
        









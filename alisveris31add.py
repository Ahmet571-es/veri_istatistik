import sqlite3
connection=sqlite3.connect("Products_list.db") 
cursor=connection.cursor()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS products (urunıd INT,ad TEXT,fiyat INT,stok INT)") 
    connection.commit()
create_table()
def alis_veris():
    def card_password():
        password=input("Lütfen 6 haneli şifrenizi giriniz : ")
        for i in range(0,1):
            if not password.isdigit():
                print("Şifreniz hatalı. Rakam giriniz...")
            elif password.isdigit():
                if len(password)!=6:
                    print("Şifreniz 6 haneli olmalıdır.")
                    break
                elif len(password)==6:
                    if password[0]=="0" or password[0]=="1" or password[0]=="2":
                        print("Güvenlik açısından 0 veya 1 veya 2 ile başlayan şifre giremessiniz.")
                        break
                    elif password[0]!="0" and password[0]!="1" and password[0]!="2":
                        if password[0]==password[1]==password[2]==password[3]==password[4]==password[5]:
                            print("Tüm değerler aynı olamaz. Şifre hatalı..")
                            break
                        elif password[0]!=password[1]!=password[2]!=password[3]!=password[4]!=password[5]: 
                            if password[0]==password[1]==password[2]==password[3]==password[4]:
                                print("ilk 5 değer aynı olamaz. Şifre hatalı..")
                                break
                            elif password[0]!=password[1]!=password[2]!=password[3]!=password[4]:
                                if password[0]==password[1]==password[2]==password[3]:
                                    print("ilk 4 değer aynı olamaz. Şifre hatalı..")
                                    break
                                elif password[0]!=password[1]!=password[2]!=password[3]:
                                    if password[0]==password[1]==password[2]:
                                        print("ilk 3 değer aynı olamaz. Şifre hatalı..")
                                        break
                                    elif password[0]!=password[1]!=password[2]:
                                        if password[1]==password[2]==password[3]:
                                            print("Hatalı şifre..")
                                            break
                                        elif password[1]!=password[2]!=password[3]:
                                            if password[3]==password[4]==password[5]:
                                                print("son 3 değer eşit olamaz. Şifre hatalı...")
                                                break
                                            elif password[3]!=password[4]!=password[5]:
                                                if password[1]==password[2] or password[2]==password[3] or password[3]==password[4] or password[4]==password[5]:
                                                    print("Hatalı şifre. Ard arda değerler eşit olamaz.")
                                                elif password[1]!=password[2] and password[2]!=password[3] and password[3]!=password[4] and password[4]!=password[5]:
                                                    print(f"Şifreniz onaylandı...")
                                                    def para_yatır():
                                                        money=int(input("Kartınıza yatırmak istediğiniz miktarı giriniz : "))
                                                        for i in range(0,1):
                                                            if money<0 or money<500 or money>4000:
                                                                print("Ytırma işlemi maalesef gerçekleşmedi")
                                                            elif money >500 and money<4000:
                                                                print("Para yatırma işleminiz başarı ile gerçekleşti...")
                                                                alıs=input("Alışveriş yapmak ister misiniz? E/H")
                                                                if alıs=="H":
                                                                    print(f"Hesabınızda {money} TL bulunmaktadır.")
                                                                    print("Güle Güle")
                                                                elif alıs=="E":
                                                                    print(f"Hesabınızda {money} TL bulunmaktadır.")
                                                                    print("Ürün sepetine yönlendiriliyorsunuz...")
                                                                    def urun_listele():
                                                                        urun_list=[]
                                                                        urun_list1=[]
                                                                        cursor.execute("SELECT * FROM products") 
                                                                        liste=cursor.fetchall()
                                                                        for i in liste:
                                                                            print(f"ürün ıd numarası = {i[0]}, ürün adı = {i[1]}, ürün fiyatı = {i[2]}, ürün adeti = {i[3]}") 
                                                                        urun_kac_adet=int(input("Kaç adet ürün almak istersiniz :  "))
                                                                        for i in range(0,urun_kac_adet):
                                                                            urun_ad=input(f"{i+1} sıralı almak istediğiniz ürün adını giriniz: ")
                                                                            for j in liste:
                                                                                if j[1]==urun_ad:
                                                                                    print(f"Almak istediğiniz ürünün adı={j[1]}, fiyatı={j[2]}")
                                                                                    urun_list.append(j[2])
                                                                                    urun_list1.append(j[1])
                                                                        toplam=0
                                                                        for i in urun_list:
                                                                            toplam=toplam+i
                                                                        print(f"Toplam harcamanız={toplam}")
                                                                        kalan=money-toplam
                                                                        for i in range(0,1):
                                                                            if money>=toplam:
                                                                                print(f"Hayırlı olsun. Alışverişiniz sonucu kalan paranız={kalan}")
                                                                            
                                                                            else:
                                                                                print("Maalesef Bakiyeniz Yetmedi")
            
                                                                    urun_listele()         
                                                    para_yatır()           
    card_password()                                                                              

alis_veris()

ad="Ayşe Nur"
soyad="Bilge"
dersler=list()

for i in range(3):
    isim=input("Adınızı giriniz: ")
    soyisim=input("Soyadınızı giriniz: ")
    if ad !=isim or soyad !=soyisim:
        print("Hatalı girdiniz")
        if i == 2:
            print("lütfen daha sonra tekrar deneyin")
            break
    elif ad==isim and soyad==soyisim:
        derssayisi = int(input("Ders sayınızı giriniz(min3, max5)"))
        if derssayisi < 3:
            print("Sınıf değerini yanlış girdin :(")
        else:
            for i in range(derssayisi):
                dersler.append(input("Derslerinizi giriniz: "))
            print(dersler)
            vize = int(input(f"{dersler[0]} dersinin vize notunu giriniz: "))
            final = int(input(f"{dersler[0]} dersinin final notunu giriniz: "))
            proje = int(input(f"{dersler[0]} dersinin proje notunu giriniz: "))
            notu = int((vize * 0.3) + (final * 0.5) + (proje * 0.2))
            if notu>90:
                hnotu="AA"
                print("Tebrikler :)")
            elif 70<notu<90:
                hnotu="BB"
            elif 50<notu<70:
                hnotu="CC"
            elif 30<notu<50:
                hnotu="DD"
            elif notu<30:
                hnotu="FF"
                print("Kaldınız :(")

            print(f"notunuz : {notu} harf notunuz : {hnotu}")
        break











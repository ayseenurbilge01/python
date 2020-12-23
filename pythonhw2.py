ad=input("Adınız:")
soyad=input(("Soyadınız:"))
yas=int(input("Yaşınız:"))
dt=int(input("Doğum Tarihiniz(Sadece yıl):"))
bilgi =list()
bilgi.append(ad)
bilgi.append(soyad)
bilgi.append(yas)
bilgi.append(dt)
print("Bilgileriniz: ")
for i in bilgi:
    print(i)
if yas<18:
        print("Yaşınız 18 yaşın altında, tehlikeli olduğundan dışarı çıkamazsınız")
else:
        print("Sokağa çıkabilirsiniz")
ad = input("lütfen adınızı giriniz :")
print("Hoşgeldin " + ad)

kelime = "bravo"
tahmin = ""
hak = 10

while True:
    harf_left = 0
    for karakter in kelime:
        if karakter in tahmin:
            print(karakter, end="")
        else:
            print("_",end="")
            harf_left += 1

    if harf_left == 0:
        print(" kazandınız")
        break

    ziyaretci = input("lütfen harf girin :")
    tahmin += ziyaretci

    if ziyaretci not in kelime:
        hak -= 1
        print("hatalı !")
        if hak!=0:
            print(f"kalan hakkınız {hak} ")

        if hak == 0:
            print("Oyunu kaybettiniz :(")
            break




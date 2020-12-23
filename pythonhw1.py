deger = list()
for i in range(5):
    d =input(f"{i+1}. değeri giriniz: ")
    deger.append(d)
    print("değerin tipi: {}".format(type(d)))
print(f"Girdiğiniz değerler : {deger}")
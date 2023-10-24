ortalamaNot = input("Lütfen Ortalamanızı Giriniz.")
print(type(ortalamaNot))

ortalamaNotAsInteger = int(ortalamaNot)
print(type(ortalamaNotAsInteger))

if ortalamaNotAsInteger > 80 :
    print("Geçtiniz")
elif ortalamaNotAsInteger > 50 :
    print("Başarılı")
else :
    print("Kaldınız") 

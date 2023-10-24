sayilar= [100,200,300,400, "Merhaba"] #köşeli parantez bize birden fazla değerin olduğunu idade eder. ve saymaya 0'dan başlanır. yani ben 100 değerinin printlenmesini istiyorsam 0 yazmam gerekir
print(sayilar[0])

sayilar.append(500) #listenin sonuna eleman eklmeye yarar
print(sayilar)

sayilar.remove( "Merhaba" ) #değere göre silme işlemi gerçekleştirir.
print(sayilar)

sayilar.pop() #indexe göre siler
print(sayilar)

sayilar.extend([10,20,30]) #çoklu veri ekleme
print(sayilar)

sayilar.clear() #dizinin içini temizler.
print(sayilar)


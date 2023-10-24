print("Merhaba Tobeto")

#degiskenler
#string

text = "Merhaba"
print(text)

StudentCount = "45"  #bu bir string ifadedir.

# int, integer değerler
StudentCount2 = 45
print(StudentCount2 + 5)

# double,decimal,float (ondalıklı sayılar)
averagePoint = 25.5
print(averagePoint)

#boolean, bool = true/false
İsVerified = True
print(İsVerified)

print(type(text))
print(type(StudentCount2))
print(type(averagePoint))
print(type(İsVerified))

#Matematiksel Operatörler
# + - / * %

number = 10
print(10+10)
print(number + number)

print(number - 5)

print(number / 2)

print(number * 2)

print(number % 3)

#Mantıksal Operatörler

print(number == 10)
print(number == 11)

print(number != 10) #false
print(number != 11) #true

print(number < 10) #false
print(number <=10) #true

#string interpolation

hello = "Merhaba"
userName = "Aşiyan"
totalText = hello + " " +userName   # " " ifadesi iki ifade arasında boşluk bırakılacağı anlamına gelir.
print(totalText)

totalText= "{message} {name}".format(message =hello,name="Aşiyan")
print(totalText)

#F-string
totalText= f"Hoşgeldiniz {userName}"
print(totalText)
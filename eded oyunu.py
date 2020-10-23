import random


print("Oyunumuza xosh geldiniz !!!")
a=random.randint(0,25)
print(a)
print("Aglimda 1-25 arasi eded tutmusham .Onu 5 cehdde tapmaga calish . \n1-25 arasinda eded daxil edin : ")

i=0
while i<5:
        b=int(input())
        if b in range(0,26):
            if a==b:
                print("TEBRIKLERRR DUZ TAPDINIZZZ!!!!")
                break
            if abs(a-b)<5:
                print("cox yaxinlasdiniz",abs(a-b))
            elif abs(a-b)<10:
                print("yaxinlasdiniz",abs(a-b))
            elif abs(a - b) < 15:
                print("uzaqsiniz",abs(a-b))
            elif abs(a - b) < 25:
                print("cox uzaqsiniz", abs(a - b))

        else:
            print("sehv sehv sehv")
            continue
        i=i+1

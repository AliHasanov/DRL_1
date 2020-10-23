def cem(x, y):
    return x + y


def ferq(x, y):
    return x - y


def hasil(x, y):
    return x * y


def nisbet(x, y):
    return x / y


print("Emelin novunu daxil edin :\n 1. Toplama\n 2. CIXMA\n 3. VURMA\n 4. BOLME")
while True:

         secim = input("Sechiminiz :")
         if secim in('1','2','3','4'):
             a = float(input())
             b = float(input())
             if secim == '1':
                print("Cavab :", cem(a, b))
             elif secim == '2':
                print("Cavab :", ferq(a, b))
             elif secim == '3':
                print("Cavab :", hasil(a, b))
             elif secim == '4':
                print("Cavab :", nisbet(a, b))
             break
         else: print("beynimi xarab eleme duz gir kodu")
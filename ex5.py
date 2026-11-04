a = int(input("Introduceti valoarea lui a: "))
b = int(input("Introduceti valoarea lui b: "))
suma = 0
for i in range(a, b + 1):
    suma+= i       #suma = suma + i
print("Suma numerelor de la a la n este: "+ str(suma))
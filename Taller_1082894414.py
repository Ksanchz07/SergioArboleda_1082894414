edad = 18
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#BUCLE
for i in range(5):
    print("Hola Mundo")

#while
contador = 1
while contador <= 5:
    print("Numero: " + str(contador))
    contador = contador + 1


for i in range(0, 12, 3):  
    print("Numero For; " , str (i)) 

encontrado = False
numerobuscado = 11
numeros = [1, 3, 5, 7]
for numero in numeros:
    if numero == numerobuscado:
        encontrado = True
        break
print("Numero", numerobuscado, "encontrado:", encontrado)

for i in range(3):
    for j in range(3):
        print("i:" +str(i) +" j:"+str(j))
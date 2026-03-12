# print("********************************")
# print(" Los valores del 1 al 100")
# print("********************************")

#estructura for
# for f in range(101):
#     print(f)

# print("********************************")
# print(" Los valores del 1 al 100")
# print("********************************")
#numbers pares
# for x in range(101):
#     if x%2==0:
#         print("Numero par: ",x)

# print("********************************")
# print(" Los valores del 1 al 100")
# print("********************************")
#numbers impares
# for x in range(101):
#     if x%2!=0:
#         print("Numero impar: ",x)
    
# ingresar un numero y mostrar los numeros entre esos numeros
# print("********************************")
# print(" Los valores del 1 al 100")
# print("********************************")
# n1 = int(input("Ingrese un numero para iniciar: "))
# n2 = int(input("Ingrese otro numero para terminar: "))
# for j in range (n1,n2+1):
#     print(j)

# el incremento de 2 en 2
# print("********************************")
# print(" Los valores del 1 al 100")
# print("********************************")
# for i in range(0,101,2):
#     print(i)


# print("********************************")
# print("10 valores")
# print("********************************")
# lista=[]
# for f in range(11):
#     lista.append(int(input("Ingrese un numero para iniciar: ")))
# print("Los numeros ingresados son: ",lista)
# actividad 2
print("********************************")
n1 = 0
for j in range(10):
    number = int(input("Ingrese un numero para calcular su suma y promedio: "))
    n1 += number
print("La suma de los numeros ingresados es: ",n1)
print("El promedio de los numeros ingresados es: ",n1/10)
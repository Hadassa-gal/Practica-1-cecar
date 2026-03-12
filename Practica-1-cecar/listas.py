lis_nombres = ["hadassa","Daniel","katherine", "raquel"]
lis_nota =[10,23,33,22]
print (lis_nombres)
print (len(lis_nombres))
print("********************************")
nom = input("ingrese nombre de un estdiante: ")
lis_nombres.append(nom)
print("********************************")
print(f"El tamaño de la lista es de: {len(lis_nombres)}")

for x in lis_nombres:
    print(x)
print("********************************")
print("nombre       edad")
for nombre, edad in zip(lis_nombres,lis_nota):
    print(f"{nombre}         {edad}")
# #busqueda por index
# j= input("ingrese index del nombre que busca: ")
# for x in lis_nombres:
#     if x.index == j:
#         print("El nombre que busca es: ")

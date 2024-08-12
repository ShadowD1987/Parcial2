#desarrollar un programa que determine si en una lista no existen elementos repetido

t1 = (1,2,3,4,5,5,6)

for i in t1:

    if t1.count(i) >= 2:
       
       print(f"el argumetno que se repite en la cadena es {i}")
    

    
#desarrollar un programa que deteremine si en una lista se encuentra una cadena de caracteres con dos o mas vocales. sila cadena existe debe imprimirla y si no existe bebe imprimir "no existe"

t2=("acido clorhidrico")

if t2.count("a") + t2.count("e") + t2.count("i") + t2.count("o") + t2.count("u") >= 2:

    print(f"la cadena {t2} tiene más de dos vocales")

else:

    print("la cadena no tiene más de dos bocales")

    


#desarrollar un programa que dadas dos listas determine que elemento tiene la primera lista que no tenga la segunda lista



    


#desarrollar un algoritmo que calcule el promedio de un arreglo de reales

t3=(0,1,2,3,4,5)

s=0

for i in t3:

    s+=i

print(s/len(t3))
    


#desarrollar un algoritmo que determine la mediana de un arreglo de enteros.

b = (1,2,3,4,5,6,7,8,9,10,11)

mediana = b[(int(len(b)/2))]

print(f"la mediana de la cadena es {mediana} ")
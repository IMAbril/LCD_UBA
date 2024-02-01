#Clase
palabra = "Jujuy"
if palabra[0] == palabra[-1] and palabra[1] == palabra[-2]:
    print("Es palindromo")
else:
    print("No es palindromo")
    
i = 13
while i<= 213:
    print(i)
    i += 13
    
cant_billetes = 1
espesor = 0.11
acumulado = 0.11
altura = 67.5*1000
dias = 0
while acumulado < altura :
    cant_billetes = cant_billetes*2
    acumulado = espesor*cant_billetes
    dias += 1
    
cadena = 'auto'
capadepenapa = ''
cadena.lower()
for l in cadena:
    if l in 'aeiou':
        capadepenapa += l + 'p' + l
    else:
        capadepenapa += l
print(capadepenapa)
i=0
capadepenapa = 'o'
while i < len(cadena):
    l = cadena[i]    
    if l in 'aeiou':
        capadepenapa += l + 'p' + l
    else:
        capadepenapa += l
    i += 1
    
    
altura = 100
for i in range(10):
    altura = altura *(3/5)
    print((i+1),altura)
    
frase = 'Todos somos programadores'
frase.lower()
palabras = frase.split()
frase_t = ''
for palabra in palabras:
    palabra_t = ''
    if palabra[-1] == 'o' or palabra[-2]=='o':
        if palabra[-1] == 'o':
            palabra_t = palabra[:-1] + 'e'
        else:
            palabra_t = palabra[:-2] + 'e' + palabra[-1]
    else:
        palabra_t = palabra
    frase_t += palabra_t + ' '

def maximo(a,b):
    '''
    Devuelve el maximo
    '''
    if a>= b:
        return a
    else:
        return b
        
print(maximo(2,3))

def tachar_pares(lista):
    lista_nueva = []
    for n in lista:
        if (n%2) == 0:
            lista_nueva.append('x')
        else:
            lista_nueva.append(n)
    return lista_nueva
    
lista = tachar_pares([1,2,3,4,5])
print(lista)

#Guía
'''Ejercicios'''

#1
cant_billetes = 1
espesor = 0.11
acumulado = 0.11
altura = 67.5*1000
dias = 0
while acumulado < altura :
    cant_billetes = cant_billetes*2
    acumulado = espesor*cant_billetes
    dias += 1

#2
altura = 100
for i in range(10):
    altura = altura *(3/5)
    print((i+1),altura)

#3
frase = 'Todos somos programadores'
frase.lower()
palabras = frase.split()
frase_t = ''
for palabra in palabras:
    palabra_t = ''
    if palabra[-1] == 'o' or palabra[-2]=='o':
        if palabra[-1] == 'o':
            palabra_t = palabra[:-1] + 'e'
        else:
            palabra_t = palabra[:-2] + 'e' + palabra[-1]
    else:
        palabra_t = palabra
    frase_t += palabra_t + ' '

#4
def es_par(n):
    return (n%2==0)
    
#5
def dos_pertenece(lista):
    return (2 in lista)

#6
def pertenece(lista, elem):
    return (elem in lista)

#7
def mas_larga(lista1, lista2):
    if len(lista1) > len(lista2):
        return lista1
    else:
        return lista2
#8
def cant_e(lista):
    cant = 0
    for l in lista:
        if l == 'e':
            cant += 1
    return cant

#9
def sumar_unos(lista):
    for i in range(len(lista)):
        lista[i] += 1
    return lista

#10
def mezclar(cadena1, cadena2):
    mezcla=''
    for i in range(len(mas_larga(cadena1, cadena2))):
        if i < len(cadena1):
            mezcla += cadena1[i]
        if i < len(cadena2):
            mezcla += cadena2[i]
    return mezcla



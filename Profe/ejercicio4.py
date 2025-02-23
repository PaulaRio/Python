def promedio(lista):
    return sum(lista) / len(lista)

numeros = [
    [57, 12, 94, 44, 19],
    [58, 84, 15, 76, 44],
    [48, 58, 92, 81, 63],
    [44, 57, 19, 94, 12]
    ]

'''Utilizando una función convencional'''
print(list(map(promedio, numeros)))

'''Utilizando una función lambda'''
print(list(map(lambda lista_num: sum(lista_num) / len(lista_num),numeros)))

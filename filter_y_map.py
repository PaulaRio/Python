def esnegativo(num):
    return num<0


lista=[-9,0,3,-4,-1,8,-13]

a= filter(esnegativo,lista)

print(list(a)) 

lista=[-2,4,5,9]

def cuadrado(num):
    return num**2

b=map(cuadrado,lista)
print(list(b)) 
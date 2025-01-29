def fibonacci(n):
    '''Funcion generadora que devuelve fibonacci n'''
    a,b,contador=0,1,0
    while True:
       if contador>n:
           return
       yield a
       a,b=b,a+b
       contador += 1
   
'''Principal'''
f= fibonacci(15)
for i in f:
    print(i)
    
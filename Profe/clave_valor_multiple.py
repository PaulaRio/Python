def indeterminados_por_nombre(**parametros):
    for parametro in parametros:
        print(parametro, " ---> ", parametros[parametro])

indeterminados_por_nombre(num=36,c='hola',lista=[1,2,5])
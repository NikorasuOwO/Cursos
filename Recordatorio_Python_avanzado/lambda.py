# función lambda

# estructura -> lambda parámetro1, parámetro2, parámetro3 : sentencia

res = lambda param1, param2: param1 * param2

# Esto es equivalente a:

def res(param1, param2):
    return param1 * param2


print(str(res(2, "3")))

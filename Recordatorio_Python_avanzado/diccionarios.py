# Estructura de datos: diccionario

coche1 = {"marca":"bmw", "potencia":158, "precio":35000}
coche2 = {"marca":"porsche", "potencia":218, "precio":55000}

moto1 = {"marca":"yamaha", "potencia":211, "precio":45000}
moto2 = {"marca":"yamaha", "potencia":321, "precio":65000}

# Podemos encadenar diccionarios

vehiculos = {"coches":[coche1, coche2], "motos":[moto1, moto2]}

# Acceso al datos

print(str(vehiculos["coches"]))
print(str(coche1["marca"]))
print("\n")

# Métodos:
print(str(coche1.values()) + str(type(coche1.values()))) # .values() devuelve los valores
print(str(coche1.keys())) # .keys() devuelve las keys
print(str(coche1.items())) # .items() devuelve los pares (key, value)
print("\n")

# Uso en bucles, quermos imprimir los valores/keys/items

for a in coche2.values():
    print(str(a))
print("\n")

for a in coche2.keys():
    print(str(a))

print("\n")
for a in coche2.items():
    print(str(a))

print("\n")
for key, value in coche2.items():
    print(str(key) + " del coche: " + str(value))


# Cambiar valores
print("\n")
print(str(vehiculos))

vehiculos["motos"][0]["marca"] = "suzuki"
coche3 = {"marca":"fiat", "potencia":120, "precio": 12000}
vehiculos["coches"][0] = coche3
print("\n")
print(str(vehiculos))

# Añadir una clave
coche1["puertas"] = 4

# Borrar clave. Podemos usar .pop() o del
print(str(coche1))
coche1.pop("potencia")
print("\n" + str(coche1))

del coche1["marca"]
print("\n" + str(coche1))

coche2.clear() # Limpia COMPLETAMENTE el diccionario
print("\n" + str(coche2))

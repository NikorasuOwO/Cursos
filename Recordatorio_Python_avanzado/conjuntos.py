# Conjuntos

# crear set
Set_de_la_compra = {'manzana', 'peras', 'lentajas'}
print(Set_de_la_compra)

# acceso a los datos

for item in Set_de_la_compra:
    print(item)

print("manzana" in Set_de_la_compra)

#Añadir
Set_de_la_compra.add("naranjas")
print(Set_de_la_compra)

# Otro Set, mixing sets
set_compra2 = {'pollo', 'ternera'}
set_compra2.update(Set_de_la_compra)
print(set_compra2)
# otra opcion
set1 = {1,2,3,5}
set2 = {0,4,6,7,1}
print(set1.union(set2))
print(set1) # Set1 no se ve afectado!!
# Eliminar

set_compra2.remove('pollo')
print(set_compra2)

# limpiar
set_compra2.clear()
print(set_compra2)

# Intersection
print("\n")
set3 = set1.union(set2)
set3 = set1.intersection(set2)
print(set3)

# Elementos no comunes
set3 = set1.union(set2)
set3 = set1.symmetric_difference(set2)
print(set3)

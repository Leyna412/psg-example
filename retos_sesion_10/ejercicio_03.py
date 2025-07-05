# EJERCICIO 3 
tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

# a) Clientes que compraron en ambos canales
# Primero convertir en Set()
ambos_canales = set(tienda_fisica) & set(tienda_online)
print("Compraron en ambos canales:", ambos_canales)

#b) Clientes que compraron solo en la tienda física
solo_fisica = set(tienda_fisica) - set(tienda_online)
print("Compraron solo en tienda física:", solo_fisica)

# c)Clientes que compraron solo online
solo_online = set(tienda_online) - set(tienda_fisica)
print("Compraron solo online:", solo_online)

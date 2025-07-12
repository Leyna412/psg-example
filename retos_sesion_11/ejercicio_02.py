# Ejercicio 2
# Diccionario inicial
alimentos = {"carne": ["gato", "perro"], "zanahoria": ["conejo"]}

# Añadir 4 alimentos con update() (sin for)
alimentos.update(pescado=["gato", "hurón"], trigo=["hamster", "pájaro"], 
                 leche=["gato", "perro"], manzana=["caballo", "conejo"])

# Verificar si 'trigo' existe (sin for)
existe_trigo = "trigo" in alimentos

# Eliminar 'zanahoria' (sin for)
alimentos.pop("zanahoria", None)

# Mostrar resultados (sin for)
print("Diccionario actualizado:", alimentos)
print("¿Existe 'trigo'?", existe_trigo)
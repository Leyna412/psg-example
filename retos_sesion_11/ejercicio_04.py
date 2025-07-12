# Ejercicio 4 
# Diccionario inicial de hábitats en peligro
habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}

# 1. Añadir 2 hábitats más con update()
habitats.update({
    "sabana africana": {
        "especies": {"león", "rinoceronte"}
    },
    "arrecife coralino": {
        "especies": {"tortuga marina", "pez payaso"}
    }
})

# 2. Verificar si existe el hábitat 'amazonas'
existe_amazonas = "amazonas" in habitats
print(f"¿Existe el hábitat 'amazonas'? {existe_amazonas}")

# 3. Añadir 'anaconda' al amazonas
habitats["amazonas"]["especies"].add("anaconda")

# Mostrar el diccionario actualizado
print("\nDiccionario de hábitats actualizado:")
print(habitats)
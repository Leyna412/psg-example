# Ejercicio 1
animal_marino = {
    "especie": "Tiburón blanco",
    "habitat": "Océano abierto y costero",
    "dieta": ["peces", "focas", "calamares"],
    "estado_salud": "Excelente",
    "edad": 10,  # en años
    "responsables_cuidado": {"María López", "Carlos Ruiz", "Ana Martínez"}
}

# Para acceder a la información:
print(f"Especie: {animal_marino['especie']}")
print(f"Hábitat: {animal_marino['habitat']}")
print(f"Dieta: {', '.join(animal_marino['dieta'])}")
print(f"Estado de salud: {animal_marino['estado_salud']}")
print(f"Edad: {animal_marino['edad']} años")
print(f"Responsables de cuidado: {', '.join(animal_marino['responsables_cuidado'])}")
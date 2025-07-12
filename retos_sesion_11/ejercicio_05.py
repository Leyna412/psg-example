# Ejercicio 5
# Arca de Noé inicial
arca = {
    "🐶": 2,  # Perros
    "🐱": 2,  # Gatos
    "🐯": 2,  # Tigres
    "🐵": 2,  # Monos
    "🦄": 0,  # Unicornios (no entran en el arca)
    "🦒": 1   # Jirafas (faltaría 1)
}

# 1. Añadir 3 especies más con update()
arca.update({"🐍": 2, "🦅": 2, "🐬": 2})

# 2. Lista de animales en el arca (iterando)
animales_arca = []
for animal, cantidad in arca.items():
    animales_arca.extend([animal] * cantidad)

print("Animales en el arca:", animales_arca)

# 3. Verificar si existe 'dragon' 🐲
existe_dragon = "🐲" in arca
print("¿Existe el dragón en el arca?", existe_dragon)  # False

# 4. Eliminar unicornio 🦄
arca.pop("🦄", None)

# 5. Modificar jirafa 🦒 a 2 ejemplares
arca["🦒"] = 2

# 6. Vaciar el arca después del diluvio
arca.clear()

print("\nArca después del diluvio:", arca)
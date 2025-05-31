# Tabla de verdad: acceso con tarjeta o huella, pero no ambas a la vez (XOR)

print("Tarjeta | Huella | Puerta se abre")
print("-------------------------------")

# Recorremos todas las combinaciones posibles (2 variables booleanas)
for tarjeta in [False, True]:
    for huella in [False, True]:
        # Lógica: la puerta se abre si solo una de las dos es verdadera
        puerta_se_abre = tarjeta ^ huella
        print(f"{str(tarjeta):^8} | {str(huella):^6} | {str(puerta_se_abre):^15}")
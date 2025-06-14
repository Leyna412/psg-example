# Ingresar pregunta por teclado y almacenar en tupla
pregunta = (input("Ingrese una pregunta: "),)

# Concatenar las tuplas
tupla_concatenada = ('¿', ) + pregunta + ('?', )

# Imprimir resultado concatenado
print(tupla_concatenada)

# Repetir la tupla concatenada 2 veces
tupla_repetida = tupla_concatenada * 2

# Imprimir nuevo resultado
print(tupla_repetida)
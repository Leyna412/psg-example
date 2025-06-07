print("startswith()")
frase = "La vida es bella"
print(frase.startswith("La vida"))  
print(frase.startswith("vida")) 

print("str.encode(encoding='utf-8', errors='strict')")
mensaje = "¡Hola mundo!"
codificado = mensaje.encode()
print(codificado)  # b'\xc2\xa1Hola mundo!'

print("str.center(width[, fillchar])")
titulo = "Python"
centrado = titulo.center(20)
print(centrado)

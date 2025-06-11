print("Convierta 1000000 de segundos en semanas, días, horas, minutos y segundos")
print ("RESOLUCIÓN")
total_segundos = 1000000
print("total_segundos = 1000000")
# Conversión
print("# Conversión")
semanas = total_segundos // (7 * 24 * 60 * 60)
print("semanas = total_segundos // (7 * 24 * 60 * 60)")
resto = total_segundos % (7 * 24 * 60 * 60)

días = resto // (24 * 60 * 60)
print("días = resto // (24 * 60 * 60)")
resto = resto % (24 * 60 * 60)

horas = resto // (60 * 60)
print ("horas = resto // (60 * 60)")
resto = resto % (60 * 60)

minutos = resto // 60
print("minutos = resto // 60")
segundos = resto % 60

# Mostrar los resultados
print("# Mostrar los resultados")
print("1,000,000 segundos equivalen a:")
print(semanas, "semanas")
print(días, "días")
print(horas, "horas")
print(minutos, "minutos")
print(segundos, "segundos")
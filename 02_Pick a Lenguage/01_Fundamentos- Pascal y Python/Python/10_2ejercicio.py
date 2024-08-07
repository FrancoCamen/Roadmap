calificacion = 0

pregunta1 = input ("estas programando en python? \r\n")

if pregunta1 == "si":
    calificacion += 1
else:
    calificacion += 0

pregunta2 = input("hoy es viernes? \r\n")

if pregunta2 == "si":
    calificacion += 1
else:
    calificacion += 0

pregunta3 = input ("2 + 3 es 8? \r\n")

if pregunta3 == "no":
    calificacion += 1
else:
    calificacion += 0

print(f"tu calificacion es {calificacion}")




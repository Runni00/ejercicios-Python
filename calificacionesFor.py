#calificaciones obtenidas
malo_50 = 0
regular_50_70 = 0
bueno_70_80 = 0
exelente_80 = 0

for i in range(1, 10):
    calificacion = int(input("inserte la calificacion del estudiante"))
    
    if calificacion > 80:
        exelente_80 += 1
    elif calificacion > 70 and calificacion < 80:
            bueno_70_80 += 1 
    elif calificacion > 50 and calificacion < 70:
            regular_50_70 += 1 
    elif calificacion < 50:
            malo_50 += 1  

print(f"{malo_50} obtuvieron una calificacion menor a 50")
print(f"{bueno_70_80} obtuvieron una calificacion menor a 70 y mayor a 80")
print(f"{regular_50_70} obtuvieron una calificacion menor a 50 y mayor a 70")
print(f"{exelente_80} obtuvieron una calificacion mayor a 80")

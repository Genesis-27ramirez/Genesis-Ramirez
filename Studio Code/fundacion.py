# evento
estudiantes = [
    {"nombre": "Jonathan", "habilidades": ["diseño"], "horas": 10},
    {"nombre": "Hernandez", "habilidades": ["organización"], "horas": 15},
    {"nombre": "Hellen", "habilidades": ["diseño"], "horas": 8},
    {"nombre": "Carlos", "habilidades": ["puerta"], "horas": 18},
    {"nombre": "Angel", "habilidades": ["diseño"], "horas": 24},
    {"nombre": "Abdiel", "habilidades": ["organizacion"], "horas":  7}
]
 
# Áreas
areas = {
    "Resecion": ["puerta"],
    "Administracion": ["organización"],
    "Decoracion": ["diseño"],
}
 
# Crear lista vacía de asignaciones
asignaciones = {area: [] for area in areas}
 
# Asignar estudiantes
for estudiante in estudiantes:
    for area, habilidades in areas.items():
        if any(h in estudiante["habilidades"] for h in habilidades):
            asignaciones[area].append(estudiante)
            break
 
# Mostrar resultados
for area, lista in asignaciones.items():
    print("\nÁrea:", area)
    for persona in lista:
        print("-", persona["nombre"], "|", persona["horas"])
 







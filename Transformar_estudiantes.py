print ("Hola, aplicaciones y servicios web")

import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent
RUTA_CSV = BASE_DIR / "Datos" / "Estudiantes.csv"

print(RUTA_CSV)
print(RUTA_CSV.exists())

with open(RUTA_CSV, encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    estudiantes = list(lector)

print(f"Total de estudiantes leídos: {len(estudiantes)}")
print(estudiantes[0])


def transformar_estudiante(fila: dict) -> dict:
    """Transformación con una función """
    if fila["activo"] == "true":
        estado = "Activo"
    else:
        estado = "Inactivo"

    return {
        "id": int(fila["codigo"]),
        "nombre_completo": fila["nombre"] + " " + fila["apellido"],
        "semestre": int(fila["semestre"]),
        "promedio": float(fila["promedio"]),
        "estado": estado,
    }
estudiantes_transformados = []

for fila in estudiantes:
    estudiantes_transformados.append(transformar_estudiante(fila))

print(f"Total transformados: {len(estudiantes_transformados)}")
print(estudiantes_transformados[0])
print(estudiantes_transformados[-1])

def serializar_estudiantes(ruta: Path, estudiantes: list[dict]) -> None:
    """Serializa una lista de diccionarios Python a un archivo JSON UTF-8."""
    ruta.parent.mkdir(exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=2, ensure_ascii=False)

RUTA_JSON = BASE_DIR / "salida" / "estudiantes_resumen.json"

serializar_estudiantes(RUTA_JSON, estudiantes_transformados)
print(f"Archivo JSON generado: {RUTA_JSON}")

def deserializar_estudiantes(ruta: Path) -> list[dict]:
    """Deserializa un archivo JSON a una lista de diccionarios Python."""
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)

estudiantes_recuperados = deserializar_estudiantes(RUTA_JSON)

print("\nDatos recuperados desde el JSON:")
print(estudiantes_recuperados[0])
print(f"Total recuperado: {len(estudiantes_recuperados)}")
from pathlib import Path

BASE = Path(__file__).resolve()
print(BASE) # Carpeta de mi proyecto

raw = BASE.parent.parent / "data" / "raw"
clean = BASE.parent.parent / "data" / "clean"

#Creacion de los directorios
raw.mkdir(parents=True, exist_ok=True)
clean.mkdir(parents=True, exist_ok=True)

# Escribir en un txt
txt_path = raw/"notas.txt"
txt_path.write_text("Texto de prueba para python typing \n", encoding="utf-8")

contenido = txt_path.read_text(encoding="utf-8")
print(contenido)
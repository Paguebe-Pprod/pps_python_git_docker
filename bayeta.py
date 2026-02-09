import random

def frotar(n_frases: int = 1) -> list:
    try:
        # Abrimos el archivo de frases
        with open("frases.txt", "r", encoding="utf-8") as f:
            # Creamos una lista con las líneas que no estén vacías
            todas = [linea.strip() for linea in f.readlines() if linea.strip()]
        
        if not todas:
            return ["El archivo de frases está vacío."]

        # Elegimos N frases aleatorias (máximo las disponibles)
        n_a_sacar = min(n_frases, len(todas))
        return random.sample(todas, n_a_sacar)
        
    except FileNotFoundError:
        return ["Error: No se encontró el archivo frases.txt"]

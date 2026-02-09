import random

def frotar(n_frases: int = 1) -> list:
    try:
        with open("frases.txt", "r", encoding="utf-8") as f:
            todas_las_frases = [linea.strip() for linea in f.readlines() if linea.strip()]
        
        n_a_sacar = min(n_frases, len(todas_las_frases))
        
        return random.sample(todas_las_frases, n_a_sacar)
    except FileNotFoundError:
        return ["Error: No se encontró la fuente de sabiduría (frases.txt)"]

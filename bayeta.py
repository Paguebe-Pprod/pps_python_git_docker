from persistencia import consultar, inicializar, annadir_frases

# Inicializamos la DB al importar el módulo (por si acaso)
inicializar()

def frotar(n_frases: int = 1) -> list:
    try:
        return consultar(n_frases)
    except Exception as e:
        return [f"Error al conectar con la sabiduría de Mongo: {e}"]

def annadir(nuevas_frases: list):
    return annadir_frases(nuevas_frases)

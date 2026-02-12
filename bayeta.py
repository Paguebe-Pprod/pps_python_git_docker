from persistencia import consultar, inicializar

# Inicializamos la DB al importar el módulo (por si acaso)
inicializar()

def frotar(n_frases: int = 1) -> list:
    try:
        # Llamamos a la nueva función de persistencia en Mongo
        return consultar(n_frases)
    except Exception as e:
        return [f"Error al conectar con la sabiduría de Mongo: {e}"]

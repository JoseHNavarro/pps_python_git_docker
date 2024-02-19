import random

def frotar(n_frases: int = 1) -> list:
    #frases
    lista_de_frases = [
        "Diría que tienes buena suerte, pero no me caes muy bien, usuario anónimo.",
        "Mala suerte para ti, por listo.",
        "Tu suerte es nula.",
    ]

    frases_elegidas = random.sample(lista_de_frases, n_frases)

    return frases_elegidas


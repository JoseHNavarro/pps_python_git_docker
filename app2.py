from bayeta import frotar

if __name__ == "__main__":
    frases_aleatorias = frotar(n_frases=3)
    for frase in frases_aleatorias:
        print(frase)


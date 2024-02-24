import random
    # Tu código para generar frases aleatorias...
def frotar (n_frases: int = 1) -> list():
#	frases_aleatorias = frotar(n_frases)
	res=[]
	for frase in range(n_frases):
		file=open("frases.txt","r")
		num=random.randint(1,5)
		for i in range(num):
			linea=file.readline()
		res.append(linea)
		file.close()
	return res

    # Resto de tu código...

#if __name__ == "__main__":

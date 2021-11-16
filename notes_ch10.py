
# attribut = on peut y accéder à exterieur
#   comment accéder

# self c l'objet qu'on a
# meme si 2 objets self meme classe, ils sont totalement independants


class Velo:
	def __init__(self, color, position):  # on donne valeur en parametre
		self.__color = "bleu"  # =  attribut privé (empeche modification à exterieur)
		self.color = "bleu"  # =  attribut public
		self.position = 0

	def avance(self):
		self.position += 1


if __name__ == "__main__":
	velo = Velo("rouge", 10) # reference a def ()


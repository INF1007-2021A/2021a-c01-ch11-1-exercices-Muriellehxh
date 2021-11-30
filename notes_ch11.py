# attribut = on peut y accéder à exterieur
#   comment accéder

# self c l'objet qu'on a
# meme si 2 objets self meme classe, ils sont totalement independants


class Velo:
    def __init__(self, color, position=0):  # on donne valeur en parametre
        self.__color = "bleu"  # =  attribut privé (empeche modification à exterieur)
        self.color = "bleu"  # =  attribut public
        self.position = 0

    def avance(self):  # methode
        self.position += 1

    @staticmethod
    def infovalue():
        print("mot")

    def __add__(self, other):
        return self.position + other.position

    @color.setter
    def color(self, value):
        if type(value) == str:
            self.__color = value


class Personne():
    def __init__(self, nom, age):  # method with attributes in () en parametres
        self.name = nom
        self.age = age


nom_instance = Personne("Mario", "2") # class name ( attribute values )

print(x.name)

if __name__ == "__main__":
    velo = Velo("rouge", 10)  # reference a def ()

    velo1 = Velo()
    velo2 = Velo("rouge")
    # si on veut additioner v1 et v2

    print(velo1 + velo2)  # while using def __add__

# error in yellow??

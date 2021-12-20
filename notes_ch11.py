# attribut = on peut y accéder à exterieur
#   comment accéder

# self c l'objet qu'on a
# meme si 2 objets self meme classe, ils sont totalement independants

# TODO: Composition vs agrégation:
# Composition = dépendance entre 2 objets
# Agrégation = pas de dépendance entre 2objets  <== + utilisé par python

# TODO: Surchage:
# Opérations des méthodes avec syntaxe spéciale
# TODO: NOTER DIAPOSITIVES 21 & 22 !! (TABLEAU SURCHAGES)



class Velo():
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




# Méthode destructrice
    roues = [1, 2, 3]
    def __del__(self):
        print('Je me suis détruis')

class Personne():
    def __init__(self, nom, age):  # method with attributes in () en parametres
        self.name = nom
        self.age = age


class Puissance2():
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration # j'ai terminé

numbers = Puissance2(3)
i = iter(numbers)
print(next(i))
print(next(i))

if __name__ == "__main__":
    velo = Velo("rouge", 10)  # reference a def ()

    velo1 = Velo('bleu')
    velo2 = Velo("rouge")
    # si on veut additioner v1 et v2

    print(velo1 + velo2)  # while using def __add__
    # error in yellow??

    # TODO: Notes sur relation objet - classe:

    monVelo = Velo('rouge')
    print(type(monVelo))  # will print Velo
    # le nom d'une classe représente le type de son objet

    # TODO: Objet = produit / sortie d'une classe, DONC, c une instance d'objet


# Classe Personne

    nom_instance = Personne("Mario", "2")  # class name ( attribute values )



# TODO: notes sur properties

' @property sert à accéder à attribut privé à extérieur de def '
' @setproperty sert à accéder à attribut privé ET modifier aattribut '


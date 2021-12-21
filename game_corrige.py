

"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import random

import utils


class Weapon:
    """
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

    def __init__(self, weapon_name: str, power: int, min_level: int):
        self.__weapon_name = weapon_name  # ne peut etre changé
        self.power = power
        self.min_level = min_level

    def make_unarmed(self):
        return self.__init__("Unarmed", 20, 1)


    @property  # pour accéder à attribut privé, comme dans def en haut
    def weapon_name(self):
        return self.__weapon_name


class Character:   # TODO: DONT MAKE WEAPON une classe fille, car character va  QUE  hériter de Weapon, mais va PAS contenir weapon
                           # TODO: on a besoin de en paramètre de character (weapon: Weapon)

    """
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

    def __init__(self, name, max_hp, attack, defense, level, weapon: Weapon):

        self.__name = name
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.level = level
        self.weapon = weapon
        self.hp = max_hp   # TODO: quand on modifie un attribut avec @hp.setter, faut mettre un @property, car hp.setter rend hp un attribut privé

    @property  # to use self.__name outside of innit
    def name(self):
        return self.__name


    def compute_damage(self, defender: "Character"):
        rand_crit = random.choices([1, 2], weights=(93.75, 6.25), k=1)
        rand_crit_num = ''.join(str(e) for e in rand_crit)
        rand_num = random.uniform(0.85, 1)
        print(rand_num)
        return ((((2 / 5) * float(self.level) + 2) * float(self.weapon.power) * float(self.attack / defender.defense)) / 50 + 2) * float(float(rand_crit_num) * rand_num)


def deal_damage(attacker, defender):
    # TODO: Calculer dégâts

    damage = Character.compute_damage(attacker, defender)
    return f"{attacker.name} used {attacker.weapon.weapon_name} \n" \
           f"   {defender.name} took {damage} dmg"


def run_battle(c1, c2):
    # TODO: Initialiser attaquant/défendeur, tour, etc.
    attacker = c1
    defender = c2



c1 = Character("Äpik", 200, 150, 70, 70)
c2 = Character("Gämmor", 250, 100, 120, 60)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)

deal_damage(c1, c2)

print(run_battle(c1, c2))
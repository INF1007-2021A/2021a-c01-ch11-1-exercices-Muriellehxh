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

	UNARMED_POWER = 20


class Character(Weapon):
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level, weapon_name: str, power: int, min_level: int):
		super().__init__(weapon_name, power, min_level)

		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon_name



	def compute_damage(self, defender: "Character"):
		rand_crit = random.choices([1, 2], weights=(93.75, 6.25), k=1)
		rand_crit_str = ''.join(str(e) for e in rand_crit)
		rand_num = random.randrange(85, 100)
		return (( ( (2/5) * float(self.level) + 2 )* float(self.power) * float(self.attack/defender.defense))/50 + 2) * float(rand_crit_str * rand_num)


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts

	damage = Character.compute_damage(attacker, defender)
	return f"{attacker.name} used {attacker.weapon} \n" \
		   f"   {defender.name} took {damage} dmg"


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass


c1 = Character("Äpik", 200, 150, 70, 70, "BFG", 100, 69)
c2 = Character("Gämmor", 250, 100, 120, 60, "Deku Stick", 120, 1)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)

deal_damage(c1, c2)
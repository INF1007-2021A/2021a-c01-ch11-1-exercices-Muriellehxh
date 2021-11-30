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

		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.hp = max_hp

	def compute_damage(self, defender: "Character"):
		return (( ( (2/5) * self.level + 2 )* self.power * (self.attack/defender.defense))/50 +2) * ()


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	pass


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass

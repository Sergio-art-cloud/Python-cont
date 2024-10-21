

import random

class Hero:
    def __init__(self, name, health, armor, strong):
        self.name = name  # attribute that saves name
        self.health = health  # attribute that saves health
        self.armor = armor  # attribute that saves armor
        self.strong = strong  # attribute that saves strength

    def print_info(self):
        print(f'Hero: {self.name}')
        print(f'Health: {self.health}')
        print(f'Armor: {self.armor}')
        print(f'Strength: {self.strong}')

    def kick(self, enemy, power_of_hit=1):
        damage = self.strong * power_of_hit
        if damage > 0:
            enemy.health -= damage
            print(f'{self.name} hit {enemy.name}: {damage}')
        else:
            print(f'{enemy.name} blocked hit from {self.name}')

        self.print_info()
        enemy.print_info()

    def fight(self, enemy):
        print(f'FIGHT between {self.name} and {enemy.name}')
        print()
        while self.health > 0 and enemy.health > 0:
            first_attack = random.choice([self, enemy])
            second_attack = enemy if first_attack == self else self
            print(f'{first_attack.name} attacked first')
            first_attack.kick(second_attack)

            if second_attack.health <= 0:
                print(f'{second_attack.name} was defeated')
                break

            print()
            print(f'{second_attack.name} will attack')

            if first_attack.health <= 0:
                print(f'{first_attack.name} was defeated')
                break


class Arena:
    def __init__(self):
        self.warriors = []

    def add_warrior(self, warrior):
        if warrior in self.warriors:
            raise ValueError('Warrior already in the arena')
        else:
            self.warriors.append(warrior)
            print(f'{warrior.name} takes part in battle')

    def battle(self):
        if len(self.warriors) < 2:
            raise ValueError('The number of warriors must be more than one')

        while len(self.warriors) > 1:
            invader = random.choice(self.warriors)
            defender = random.choice([w for w in self.warriors if w != invader])

            print(f'{invader.name} is attacking {defender.name}')
            invader.kick(defender)

            if defender.health <= 0:
                print(f'{defender.name} fell in battle')
                self.warriors.remove(defender)

        winner = self.warriors[0]
        print(f'The warrior who won is {winner.name}')


class Mage(Hero):
    def __init__(self, name, health, armor, strong, special_points):
        super().__init__(name, health, armor, strong)
        self.special_points = special_points
        self.special_points_name = 'mana'
        self.special_points_k = 2

    def hello(self):
        print(f'Good morning, I am {self.name}, I can use poison: {self.special_points_name}')

    def special_attack(self):
        if self.special_points > 0:
            self.special_points -= 1
            damage = self.strong * self.special_points_k  # apply coefficient
            print(f'{self.name} used magic attack and dealt {damage} damage')
            return damage
        else:
            print('Not enough mana')
            return 0

    def attack(self):
        if random.random() <= 0.25 and self.special_points > 0:
            damage = self.special_attack()
            print(f'{self.name} used special attack, dealing {damage} damage')
            return damage
        else:
            damage = self.strong  # or implement your own logic
            print(f'{self.name} used a normal attack, dealing {damage} damage')
            return damage


class Ork(Hero):
    def __init__(self, name, health, armor, strong, special_points):
        super().__init__(name, health, armor, strong)
        self.special_points = special_points
        self.special_points_name = 'furia'
        self.special_points_k = 2


class Knight(Hero):
    def __init__(self, name, health, armor, strong, special_points):
        super().__init__(name, health, armor, strong)
        self.special_points = special_points
        self.special_points_name = 'courage'
        self.special_points_k = 2


# Create heroes
hero1 = Mage('Mag', 100, 30, 20, 3)
hero2 = Ork('Ork', 120, 20, 25, 2)
hero3 = Knight('Knight', 110, 40, 22, 4)

# Create an arena and add heroes
arena = Arena()
arena.add_warrior(hero1)
arena.add_warrior(hero2)
arena.add_warrior(hero3)

# Start the battle in the arena
arena.battle()

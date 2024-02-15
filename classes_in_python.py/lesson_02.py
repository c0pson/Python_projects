class Character:

    level = 1
    characters_on_map = 0

    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name
        Character.characters_on_map += 1

    def print_stats(self):
        print(f'{self.name} stats: Health: {self.health} | Damage: {self.damage} | Level: {self.level}')

    def level_up(self):
        self.level += 1

print(Character.characters_on_map)

yeti = Character(health=200, damage=15, name='Yeti')
print(yeti.__dict__)
print(Character.characters_on_map)

lizard = Character(health=100, damage=40, name='Lizard')
print(Character.characters_on_map)

yeti.level_up()
print(yeti.__dict__)
yeti.level_up()
lizard.level_up()

yeti.print_stats()
lizard.print_stats()

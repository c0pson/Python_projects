class Character:

    level = 1

    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name

    def print_stats(self):
        print(f'{self.name} stats: Health: {self.health} | Damage: {self.damage} | Level: {self.level}')

    def level_up(self):
        self.level += 1

yeti = Character(health=200, damage=15, name='Yeti')
lizard = Character(health=100, damage=40, name='Lizard')

# yeti.print_stats()
# lizard.print_stats()

yeti.level_up()
yeti.level_up()
lizard.level_up()

yeti.print_stats()
lizard.print_stats()

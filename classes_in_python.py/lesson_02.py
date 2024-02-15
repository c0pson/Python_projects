class Character:

    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name

    def print_stats(self):
        print(f'{self.name} stats: Health: {self.health} | Damage: {self.damage}')

yeti = Character(health=200, damage=15, name='Yeti')
lizard = Character(health=100, damage=40, name='Lizard')

print(yeti)
print(lizard)

yeti.print_stats()
lizard.print_stats()

import time
import datetime

class Character:

    xp_multiplier = 1
    character_level = 1
    characters_on_map = 0
    time_started_playing = time.time()

    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name
        Character.characters_on_map += 1

    def print_stats(self):
        print(f'{self.name} stats: Health: {self.health} | Damage: {self.damage} | Level: {self.character_level} | Xp multiplier: {self.xp_multiplier}')

    def level_up(self):
        self.character_level += 1

    @classmethod
    def xp_multiplier_raise(cls, amount):
        cls.xp_multiplier = amount

    @classmethod
    def play_time(cls, now):
        print(now - cls.time_started_playing)

    @staticmethod
    def week_promotion(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print('Weekend promotion is open')
            return True
        print('Weekend promotion is closed')
        return False

yeti = Character(health=200, damage=15, name='Yeti')
lizard = Character(health=100, damage=40, name='Lizard')

print(Character.xp_multiplier)

Character.xp_multiplier_raise(1.5)

print(Character.xp_multiplier)
print(yeti.xp_multiplier)
print(lizard.xp_multiplier)

time.sleep(2)

Character.play_time(time.time())

Character.week_promotion(datetime.date(2024, 11, 16)) # saturday
Character.week_promotion(datetime.date(2024, 11, 18)) # monday

Character.play_time(time.time())
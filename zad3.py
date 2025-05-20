class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        ###obrazenia muszą być liczbą całkowitą
        self.hp = self.hp - int(amount)
        if self.hp < 0:
            self.hp = 0

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self, target):
        ###obrażenia zaokrąglane do liczby całkowitej
        damage = int(self.strength * 1.5)
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            target.take_damage(25)
            self.mana -= 10
        else:
            print("Not enough mana!")

def simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)

    print("Start:", w.hp, m.hp)
    w.attack(m)
    m.attack(w)
    m.attack(w)

    assert m.hp == 45, f"HP maga powinno wynosić 45, a wynosi {m.hp}"
    assert m.mana == 0, f"Mana maga powinna wynosić 0, a wynosi {m.mana}"

    m.attack(w)
    m.attack(w)
    print("End:", w.hp, m.hp)

simulate_battle()
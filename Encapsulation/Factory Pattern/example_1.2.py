class Character:
    def __init__(self, name):
        self.name = name

class Warrior(Character):
    def __str__(self):
        return f"Warrior: {self.name}"

class Mage(Character):
    def __str__(self):
        return f"Mage: {self.name}"

class Archer(Character):
    def __str__(self):
        return f"Archer: {self.name}"

class CharacterFactory:
    def create_character(self, character_type, name):
        if character_type == "Warrior" :
            return Warrior(name)
        elif character_type == "Mage" :
            return Mage(name)
        elif character_type == "Archer" :
            return Archer(name)

factory = CharacterFactory()
character1 = factory.create_character("Warrior", "Conan")
character2 = factory.create_character("Mage", "Merlin")

print(character1) # output is : Warrior: Conan
print(character2) # output is : Mage: Merlin

        


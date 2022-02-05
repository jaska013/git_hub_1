class Human:
    def __init__(self, height:float, weight:float):
        self.height = height
        self.weight = weight

    def say_aaa(self):
        return 'human says AAAAAAA'

class Male(Human):
    def say_aaa(self):
        return 'man says aaaaaa'

class Female(Human):
    def say_aaa(self):
        return 'woman says aaaaaa'

woman = Female(170,50)
man = Male(190,80)

print(man.say_aaa())
print(woman.say_aaa())
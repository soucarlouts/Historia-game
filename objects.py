class Monster:
    
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_life(self, life):
        return self.life 
    
    
    def damage(self):
        print("HGRUUAAAHH")

A1 = Monster("maammaaaco", 100.0)
print(A1.get_name(), A1.get_life(life=100.0))

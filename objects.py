class Monster:
    
    def __init__(self, name, age, life):
        self.name = name
        self.age = age
        self.life = life

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age
    
    def set_life(self, life):
        self.life = life
    
    def damage(self):
        print("HGRUUAAAHH")

Arvore = Monster("Nome: Samambaia\nIdade:", 10)
print(Arvore.get_name(),Arvore.get_age())

A2 = Monster("\nNome: Billa\nIdade:", 18)
print(A2.get_name(), A2.get_age())

A3 = Monster("Idade: \nmacaco\n", 180)
print (A3.get_age(), A3.get_name())

   
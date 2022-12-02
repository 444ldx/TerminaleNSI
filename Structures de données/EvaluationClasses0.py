import math as m

# Exercice 1

class Intervalle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def is_empty(self):
        if self.b < self.a or self.a is None or self.b is None:
            return True
        return False
    
    def __str__(self):
        return f"{self.a}, {self.b}"
    
    def __len__(self):
        if self.is_empty():
            return 0
        return self.b - self.a
    
    def __contains__(self, x:float):
        if self.a < x and self.b > x:
            return True
        return False
    
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False
    
    def __le__(self, other):
        if self.a < other.a and self.b > other.b or other.is_empty():
            return True
        return False
    
    def insertion(self, intervalle):
        set1 = set([n for n in range(self.a, self.b+1)])
        set2 = set([n for n in range(intervalle.a, intervalle.b+1)])
        inter = list(set1 & set2)
        return Intervalle(inter[0], inter[-1])
    
    def union(self, intervalle):
        if self.a < intervalle.a:
            if self.b > intervalle.b:
                return Intervalle(self.a, self.b)
            else:
                return Intervalle(self.a, intervalle.b)
        else:
            if self.b > intervalle.b:
                return Intervalle(intervalle.a, self.b)
            else:
                return Intervalle(intervalle.a, intervalle.b)
            

# Exercice 2

class Angle():
    def __init__(self, angle:int):
        if angle < 0 or angle > 360:
            raise Exception("L'angle doit être compris entre 0 et 360 degrés.")
        self.angle = angle
        
    def __str__(self):
        return f"{self.angle} degré" if self.angle == 1 else f"{self.angle} degrés"
    
    def add(self, angle):
        self.angle = (self.angle + angle) % 360
    
    def cos(self):
        return m.cos(m.radians(self.angle))
    
    def sin(self):
        return m.sin(m.radians(self.angle))
    
if __name__ == "__main__":
    inter1 = Intervalle(50, 100)
    inter2 = Intervalle(70, 120)
    inter3 = Intervalle(50, 100)
    
    angle0 = Angle(350)
    angle0.add(20)
    print(angle0)
class Forma:
  def calcular_area(self):
    pass

class Quadrado(Forma):
  def __init__(self, lado):
    self.lado = lado

  def calcular_area(self):
    return self.lado * self.lado

class Circulo(Forma):
  def __init__(self, raio):
    self.raio = raio

  def calcular_area(self):
    return 3.14 * (self.raio * self.raio)

forma = [Quadrado(4), Circulo(3)]
for formas in forma:
  print(formas.calcular_area())

class Cafeteira:
  def __init__(self, marca, cor, voltagem, capacidade_litros, status):
    self.marca = marca
    self.cor = cor
    self.voltagem = voltagem
    self.capacidade_litros = capacidade_litros
    self.status = False

  def ligar(self):
    self.status += True

  def fazer_cafe(self):
    print("Fazendo café...")

  def verificar_status(self):
    if self.status == True:
      print("Ligada!")
    else:
      print("Desligada!")

espresso = Cafeteira("Oster")

espresso.ligar()
espresso.verificar_status()

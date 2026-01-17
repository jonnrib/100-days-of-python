class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def show_info(self):
    print(f"{self.brand} - {self.model}")

class Car(Vehicle):
  def __init__(self, brand, model, door_count):
    super().__init__(brand, model)
    self.door_count = door_count

  def show_details(self):
    print(f"This car has {self.door_count} doors.")

class Motorcycle(Vehicle):
  def __init__(self, brand, model, engine_cc):
    super().__init__(brand, model)
    self.engine_cc = engine_cc

  def show_details(self):
    print(f"This motorcycle has {self.engine_cc} cc.")

commuter_car = Car("Toyota", "Corolla", 4)
work_truck = Car("Ford", "Ranger", 4)
sport_bike = Motorcycle("Kawasaki", "Ninja 400", 400)

commuter_car.show_info()
commuter_car.show_details()

sport_bike.show_info()
sport_bike.show_details()

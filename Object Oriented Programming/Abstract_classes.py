from abc import ABC, abstractmethod

# 1. The Abstraction (The Blueprint)
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# 2. Concrete Implementation A
class Car(Vehicle):
    def start_engine(self):
        return "Car engine turns over: Vroom vroom!"

# 3. Concrete Implementation B
class ElectricScooter(Vehicle):
    def start_engine(self):
        return "Scooter powers on: Beep. Silent readiness."

# --- Using the Abstraction ---
# You can interact with any vehicle the exact same way without caring what kind it is
def operate_vehicle(vehicle: Vehicle):
    print(vehicle.start_engine())

my_car = Car()
my_scooter = ElectricScooter()

operate_vehicle(my_car)      # Output: Car engine turns over: Vroom vroom!
operate_vehicle(my_scooter)  # Output: Scooter powers on: Beep. Silent readiness.

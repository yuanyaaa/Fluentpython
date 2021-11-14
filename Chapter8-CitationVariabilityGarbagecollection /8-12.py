class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers=passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(["Alice", "Bill"])
bus1.pick("Charlie")
bus1.drop("Alice")
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick("Charaaa")
print(bus2.passengers)

bus3 = HauntedBus()
bus3.pick("Davvv")
print(bus3.passengers)
print(bus2.passengers)
print(bus1.passengers)
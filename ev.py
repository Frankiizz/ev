import logging


class EV:
    def __init__(self, discharge=0.15, init_battery=20, capacity=40):
        self.discharge = discharge
        self.battery = init_battery
        self.capacity = capacity
        self.cost = 0

    def drive(self, driving_distance):
        print(f"|Before drive battery: {self.battery}")
        if self.battery - self.discharge * driving_distance < 0:
            print("Out of Battery !")
        else:
            self.battery -= self.discharge * driving_distance
            print(f"*drove: {driving_distance}, used: {driving_distance * self.discharge}")
        print(f"|After drive battery: {self.battery}")

    def charge(self, charge, price):
        print(f"\n|Before charge battery: {self.battery}")
        if self.battery + charge > self.capacity:
            print("Overcharged !")
        else:
            self.battery += charge
            self.cost += charge * price
            print(f"*charged: {charge} with price: {price}")
        print(f"|After charge battery: {self.battery}")



    def daily_max_charge(self):
        return self.capacity - self.battery

    def daily_max_drive(self):
        return self.battery / self.discharge

    # def display(self, dayIndex):
    #     print(f"\nDay: {dayIndex}: \nbattery: {self.battery}\ncost: ${self.cost/100}")



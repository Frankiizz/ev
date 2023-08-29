from dataLoader import load_excel
from ev import EV
import matplotlib.pyplot as plt


# Strategies:
# 1. if the current price is lower than critical price, charge till fill
# 2. if the battery is not enough for today, charge till enough.
# 3. don't charge otherwise


def plot(x, y):
    plt.plot(x, y)
    plt.xlabel('critical price(cent)')
    plt.ylabel('annual cost($)')
    plt.title('Annual costs vs critical prices')
    plt.grid(True)
    plt.show()


class Main:

    def __init__(self, cp):
        self.data = load_excel('data/off-peak_price_base.xlsx')
        self.date = self.data[0][1:]
        self.opp = list(map(float, self.data[1][1:]))
        self.ev = EV()
        self.dayIndex = 0
        self.criticalPrice = cp

    # define strategies here.
    def run_one_day(self):
        self.ev.drive(30)

        if self.opp[self.dayIndex] < self.criticalPrice:
            self.ev.charge(self.ev.daily_max_charge(), price=self.opp[self.dayIndex])
            print('case 1')


        elif self.ev.daily_max_drive() < 30:
            self.ev.charge(30 * self.ev.discharge, price=self.opp[self.dayIndex])
            print('case 2')


        else:
            print("Didn't charge")
        self.dayIndex += 1

    def run(self):
        for i in range(len(self.date)):
            print(f"-Day {self.dayIndex}")
            self.run_one_day()
            print('\n')
        print(f"total cost: {round(self.ev.cost/100, 3)}")
        return round(self.ev.cost / 100, 3)



costs = []

# cp range
for i in range(-10, 50):
    main = Main(i)
    costs.append(main.run())

plot(range(-10, 50), costs)

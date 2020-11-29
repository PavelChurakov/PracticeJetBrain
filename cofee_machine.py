class CoffeeMachine:
    def __init__(self, water, milk, coffee, cops, money, state):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cops = cops
        self.money = money
        self.state = state

    def read_options(self):
        option = input("Write action (buy, fill, take, remaining, exit):")
        if option == "buy":
            self.state = "buy"
            self.buy()
        elif option == "fill":
            self.state = "fill"
            self.fill()
        elif option == "take":
            self.state = "take"
            self.take()
        elif option == "remaining":
            self.state == "remaining"
            self.print_provision()
        elif option == "exit":
            self.state = "exit"
        else:
            print("Incorrect task")

    def buy(self):
        type_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if type_coffee == "1" and self.check_resource(250, 0, 16, 1):
            self.water -= 250
            self.coffee -= 16
            self.cops -= 1
            self.money += 4
            self.state = "action"
        elif type_coffee == "2" and self.check_resource(350, 75, 20, 1):
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cops -= 1
            self.money += 7
            self.state = "action"
        elif type_coffee == "3" and self.check_resource(200, 100, 12, 1):
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cops -= 1
            self.money += 6
            self.state = "action"
        elif type_coffee == "back":
            self.state = "action"
            self.read_options()

    def check_resource(self, w, m, c, cop):
        if self.water < w:
            print("Sorry, not enough water!")
            return False
        elif self.milk < m:
            print("Sorry, not enough milk!")
            return False
        elif self.coffee < c:
            print("Sorry, not enough coffee!")
            return False
        elif self.cops < cop:
            print("Sorry, not enough cops!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True

    def fill(self):
        water = int(input("Write how many ml of water do you want to add:"))
        self.water += water
        milk = int(input("Write how many ml of milk do you want to add:"))
        self.milk += milk
        coffee = int(input("Write how many grams of coffee beans do you want to add:"))
        self.coffee += coffee
        cops = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cops += cops

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def print_provision(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.coffee))
        print("{} of disposable cups".format(self.cops))
        print("{} of money".format(self.money))

    def run_coffee_machine(self):
        while not self.state == "exit":
            self.read_options()


if __name__ == "__main__":
    coffe_machine = CoffeeMachine(400, 540, 120, 9, 550, "action")
    coffe_machine.run_coffee_machine()


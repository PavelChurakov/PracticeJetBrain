import random
import sqlite3


class Bank:
    IIN = "400000"
    FIRST_ACC_IDENT = "000000000"

    def __init__(self, bank_name):
        self.bank_name = bank_name

    def create_account(self):
        sql = "SELECT * FROM card"
        cur.execute(sql)
        data_user = cur.fetchall()
        ACC_NUMBER = len(data_user) + 1
        acc_ident = "0" * (9 - len(str(ACC_NUMBER))) + str(ACC_NUMBER)
        first_num = self.IIN + acc_ident
        s = 0
        for i in range(len(first_num)):
            if i % 2 == 0:
                if int(first_num[i]) * 2 > 9:
                    s += (int(first_num[i]) * 2) - 9
                else:
                    s += int(first_num[i]) * 2
            else:
                s += int(first_num[i])
        if s % 10 != 0:
            check_sum = 10 - (s % 10)
        else:
            check_sum = 0
        card_num = self.IIN + acc_ident + str(check_sum)
        pin = ""
        for i in range(4):
            pin += str(random.randint(0, 9))
        balance = 0
        sql = "INSERT INTO card VALUES({0},'{1}','{2}',{3})".format(ACC_NUMBER, card_num, pin, balance)
        cur.execute(sql)
        conn.commit()
        print("Your card has been created")
        print("Your card number:")
        print(card_num)
        print("Your card PIN:")
        print(pin)

    def add_income(self, card_num):
        income = int(input("Enter income:"))
        sql_sell = "SELECT * FROM card WHERE number = '{}'".format(card_num)
        cur.execute(sql_sell)
        balance = cur.fetchone()[3] + income
        sql_update = "UPDATE card SET balance = {1} WHERE number = '{0}'".format(card_num, balance)
        cur.execute(sql_update)
        conn.commit()
        print("Income was added!")

    def close_acc(self, card_num):
        sql_dell = "DELETE FROM card WHERE number = '{0}'".format(card_num)
        cur.execute(sql_dell)
        conn.commit()
        print("The account has been closed!")

    def do_transfer(self, card_num):
        print("Transfer")
        print("Enter card number:")
        number_to = input()
        if len(number_to) == 16:
            s = 0
            for i in range(15):
                if i % 2 == 0:
                    if int(number_to[i]) * 2 > 9:
                        s += (int(number_to[i]) * 2) - 9
                    else:
                        s += int(number_to[i]) * 2
                else:
                    s += int(number_to[i])
            if (s + int(number_to[15])) % 10 != 0:
                print("Probably you made a mistake in the card number. Please try again!")
                return True
        sql_from = "SELECT * FROM card WHERE number = '{0}' ".format(card_num)
        cur.execute(sql_from)
        data_from = cur.fetchone()
        sql_to = "SELECT * FROM card WHERE number = '{0}' ".format(number_to)
        cur.execute(sql_to)
        data_to = cur.fetchone()
        if data_to is None:
            print("Such a card does not exist.")
        else:
            print("Enter how much money you want to transfer:")
            sum_trans = int(input())
            if sum_trans > data_from[3]:
                print("Not enough money!")
            else:
                rest_sum_from = data_from[3] - sum_trans
                sql_from_update = "UPDATE card SET balance = {1} WHERE number = '{0}'".format(card_num, rest_sum_from)
                cur.execute(sql_from_update)
                rest_sum_to = data_to[3] + sum_trans
                sql_to_update = "UPDATE card SET balance = {1} WHERE number = '{0}'".format(number_to, rest_sum_to)
                cur.execute(sql_to_update)
                conn.commit()
                print("Success!")

    def run_card_option(self, card_num):
        text = "1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit"
        print(text)
        option = input()
        sql = "SELECT * FROM card WHERE number = '{}'".format(card_num)
        cur.execute(sql)
        data_user = cur.fetchone()
        if option == "1":
            print("Balance: ", data_user[3])
            return True
        elif option == "2":
            self.add_income(card_num)
            return True
        elif option == "3":
            self.do_transfer(card_num)
            return True
        elif option == "4":
            self.close_acc(card_num)
            return False
        elif option == "5":
            print("You have successfully logged out!")
            return False
        else:
            return False

    def log_in_account(self):
        card_num = input("Enter your card number:")
        pin = input("Enter your PIN:")
        sql = "SELECT * FROM card WHERE number = '{}' AND pin = '{}'".format(card_num, pin)
        cur.execute(sql)
        data_user = cur.fetchone()
        if data_user is None:
            print("Wrong card number or PIN!")
            return True
        elif data_user[2] == pin:
            print("You have successfully logged in!")
            while True:
                if not self.run_card_option(card_num):
                    break
            return True
        else:
            print("Wrong card number or PIN!")
            return True

    def run_bank_terminal(self):
        while True:
            text = "1. Create an account\n2. Log into account\n0. Exit"
            print(text)
            option = input()
            if option == "1":
                self.create_account()
            elif option == "2":
                self.log_in_account()
            elif option == "0":
                print("Bye!")
                break


if __name__ == "__main__":
    bank = Bank("CHURAKOV")
    try:
        conn = sqlite3.connect("card.s3db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS "
                    "card(id INTEGER, "
                    "number TEXT,"
                    "pin TEXT, "
                    "balance INTEGER DEFAULT 0)")
        conn.commit()
        bank.run_bank_terminal()
    except EOFError:
        pass

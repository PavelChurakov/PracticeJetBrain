# Write your code here
import random

lose = "Sorry, but the computer chose {}"
draw = "There is a draw ({})"
win = "Well done. The computer chose {} and failed"


def raitings_dict():
    file_r = open("rating.txt", 'r')
    raitings = file_r.read()
    dict_raitings = {}
    if len(list(raitings)) > 0:
        for rait in raitings.split("\n"):
            if len(rait.split()) != 0:
                user_name = rait.split()[0]
                user_score = int(rait.split()[1])
                dict_raitings[user_name] = user_score
    file_r.close()
    return dict_raitings


def change_raiting(name_user, raiting):
    dict_raitings = raitings_dict()
    file_r = open("rating.txt", 'w+')
    if name_user in dict_raitings:
        dict_raitings[name_user] += raiting
    else:
        dict_raitings[name_user] = raiting
    for key, value in dict_raitings.items():
        file_r.write("{0} {1}\n".format(key, value))
    file_r.close()


def return_raiting(name_user):
    dict_raitings = raitings_dict()
    if name_user in dict_raitings:
        return dict_raitings[name_user]
    else:
        return 0


def check_winer_new(user_name, user_ch, computer_ch, list_options):
    if user_ch in list_options:
        lst_options_for_work = list_options[:]
        i = lst_options_for_work.index(user_ch)
        del lst_options_for_work[i]
        sub_list = lst_options_for_work[i:] + lst_options_for_work[:i]
        j = len(sub_list) // 2
        list_more = sub_list[:j]
        list_less = sub_list[j:]
        if computer_ch in list_more:
            change_raiting(user_name, 0)
            return lose.format(computer_ch)
        elif computer_ch in list_less:
            change_raiting(user_name, 100)
            return win.format(computer_ch)
        elif computer_ch == list_options[i]:
            change_raiting(user_name, 50)
            return draw.format(computer_ch)
    elif user_ch == "!exit":
        return "Bye!"
    elif user_ch == "!rating":
        return "Your rating: {}".format(str(return_raiting(user_name)))
    else:
        return "Invalid input"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print("Hello, {}".format(name))
    lst_option = input()
    if len(lst_option) == 0:
        lst_option = ["rock", "paper", "scissors"]
    else:
        lst_option = lst_option.split(sep=',')
    print("Okay, let's start")
    try:
        file_ = open("rating.txt", 'r')
        file_.close()
    except:
        file_ = open("rating.txt", 'w+')
        file_.close()
    while True:
        choice_u = input()
        computer_c = random.choice(lst_option)
        text = check_winer_new(name, choice_u, computer_c, lst_option)
        if text == "Bye!":
            print(text)
            break
        else:
            print(text)

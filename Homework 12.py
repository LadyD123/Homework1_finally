import json
import datetime
import random

player = input("Hello, please enter your name? ")

def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    attempts_list = get_score_list()

while True:
    guess = int(input("Guess the secret number (between 1 and 30):"))
    attempts +=1

    if guess == secret:
        attempts_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player,
                           "secret_number": secret})
        with open("attempts_list.json", "w") as attempts_file:
            attempts_file.write(json.dumps(attempts_list))

        print("That is right - The number is " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

def get_score_list():
    with open("attempts_list.json", "r") as score_file:
        attempts_list = json.loads(attempts_file.read())
        return attempts_list

def get_top_scores():
    attempts_list = get_score_list()
    top_score_list = sorted(attempts_list, key=lambda k: k['attempts'])[:3]
    return top_score_list

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break
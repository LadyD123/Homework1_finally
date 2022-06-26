import json
import datetime
import random

player = input("Hello, please enter your name? ")

secret = random.randint(1, 30)
attempts = 0

with open("attempts_list.json","r") as attempts_file:
    attempts_list = json.loads(attempts_file.read())
    print("Your number of attempts:" + str(attempts_list))

for attempts_dict in attempts_list:
    attempts_text = "Player {0}had {1} attempts on {2}. The secret number was {3].".format(attempts_dict.get("player_name"), str(attempts_dict.get("attempts")), attempts_dict.get("date"), attempts_dict.get("secret_number"), attempts_dict.get("wrong_guesses"))
    print(attempts_text)

wrong_guesses = []
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

    wrong_guesses.append(guess)
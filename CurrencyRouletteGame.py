import urllib.request as r
import json
from random import uniform


def get_money_interval(difficulty):
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=2e015e19466c486dc19f"
    response = r.urlopen(url)
    data = json.load(response)
    ex = int(data["USD_ILS"])
    usd = int(uniform(1, 100))
    t = usd * ex
    low = int(t - (5 - difficulty))
    high = int(t + (5 - difficulty))
    return usd, t, low, high


def get_guess_from_user(usd):
    # User needs to guess the Value to a given amount of USD
    while True:
        try:
            guess = int(input(f"Guess the value of {usd}$ in ILS: "))
        except ValueError:
            print("Error: Enter just numbers ")
            continue
        return guess


def play(difficulty):
    print("Currency Roulette  game start....")

    usd, t, low, high = get_money_interval(difficulty)
    guess = get_guess_from_user(usd)
    if high >= guess >= low:
        print("you won")
        return True
    else:
        print("you lose")
        return False

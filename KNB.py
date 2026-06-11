import random

def KNB_GENERATOR(target=3):
    score_player = 0
    score_bot = 0

    def KNB(action: str):
        number = random.randint(1,3)
        bot = ""

        nonlocal target

        nonlocal score_player
        nonlocal score_bot

        if number == 1:
            bot = "камень"
        elif number == 2:
            bot = "ножницы"
        else:
            bot = "бумага"

        if action == bot:
            return f"Ничья, счет: {score_player}:{score_bot}"
        elif (action == "камень" and bot == "бумага" or 
            action == "бумага" and bot == "ножнецы" or 
            action == "ножницы" and bot == "камень"):
            score_bot += 1
            if score_bot >= target:
                return "Game over! Bot wins!"
            return f"Bot wins, score: {score_player}:{score_bot}"
        else:
            score_player += 1
            if score_player >= target:
                return "Game over! Player wins!"
            return f"Player wins, score: {score_player}:{score_bot}"
    
    return KNB




def main():
    knb = KNB_GENERATOR()
    result = ""
    while "Game over" not in result:
        action = input()
        result = knb(action)
        print(result)


if __name__ == "__main__":
    main()

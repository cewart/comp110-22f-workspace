"""Create your own adventure: cassino style 9/30/22."""

__author__ = "730551195"

player: str = ""
points: int = 0
wager: int = 0
GENIE_EMOJI: str = "\U0001F9DE"
WHITE_BOX: str = "\U00002B1C"
COWBOY_EMOJI: str = "\U0001F920"
FLYING_CASH: str = "\U0001F4B8"
FLEX_EMOJI: str = "\U0001F4AA"
ICY_EMOJI: str = "\U0001F976"
CASH_EMOJI: str = "\U0001F4B5"
BOOKS_EMOJI: str = "\U0001F4DA"
SHOE_EMOJI: str = "\U0001F97E"
SMILE_EMOJI: str = "\U0001F601"


def greet() -> None:
    """This is a procedure that greets the player to the game."""
    global player
    print(f"Hey there, welcome! My name is Chad!{GENIE_EMOJI}.")
    player = input("What is your name? ")
    print(f"Howdy {COWBOY_EMOJI}, {player}, welcome to Big Bet here's how the game works:\n")
    print(f"As a broke college student, we know you need a quick and easy way to get some cash {FLYING_CASH} {ICY_EMOJI} {FLEX_EMOJI} (without, of course, selling drugs!).\nBut we want to help! Think of this as a completely fair and totally not rigged investment opportunity!")
    return None


def chat() -> None:
    """This procedure is manipulates the global points when questions are answered."""
    global player
    global points
    print(f"Before we begin, {player}, I wanted to get to know you a bit!")
    like_college: str = input("Type 'yes' if you think Chapel Thrill is expensive, or 'no' otherwise. ")
    if like_college == "yes":
        print("Sheesh. Me too. You got 10 extra dollars just for agreeing with me!\n")
        points = points + 10
    else:
        print("Parents paying for it all, huh.\n")
    use_money: str = input(f"So, if you woud rather use this money to buy books {BOOKS_EMOJI}, type 'books', and if you would rather buy shoes, type 'shoes' {SHOE_EMOJI} ")
    if use_money == "books" or "shoes":
        print("Cool, it doesn't really matter to me what you want to spend your money on, but I'm generous, so here's $20 more. \n")
        points = points + 20
    buy_happiness: str = input("Lastly, I've got some happiness for sale if you'd like it. \nType 'buy' to spend $20 on some happiness. Type anything else to skip ")
    if buy_happiness == "buy":
        print(f"Congrats! Here's your happiness {SMILE_EMOJI} \nJust kidding, that was a ploy to get my $20 back. Can't trust anyone these days, can you?")
        points = points - 20
    return None


def slot_machine(money: int) -> int:
    """This is the (actually somewhat fair) gambling machine!"""
    global points
    global wager
    print("This slot machine takes high, medium, and low risk investments.")
    bet_level: str = input("Type 'high', 'medium', or 'low' for which risk-reward setting you'd like. ")
    wager = int(input("Now, how much of your money would you like to wager? "))
    if int(wager) > int(points):
        adjust_wager: int = int(input(f"Sorry, you currently have {points} dollars. Please input an integer less than or equal to {points}. "))
        wager = adjust_wager
    print("Good luck!")
    if bet_level == "high":
        high(wager)
    if bet_level == "medium":
        medium(wager)
    if bet_level == "low":
        low(wager)
    return wager 


def high(bet: int) -> int:
    """This is the slot machine's high risk, high potential reward setting."""
    global wager
    bet = int(bet)
    max_prize: int = int(bet * 2)
    from random import randint
    prize: int = randint(bet, max_prize)
    prize = bet - prize 
    plus_or_minus: int = randint(1, 2)
    if plus_or_minus == 1:
        prize = -(prize)
    print(f"Nice! You won {prize} dollars! {CASH_EMOJI}")
    wager = int(prize)
    return wager


def medium(bet: int) -> int:
    """This is the slot machine's medium risk, medium potential reward setting."""
    global wager
    bet = int(bet)
    max_prize: int = int(wager * 1.5)
    from random import randint
    prize: int = randint(wager, max_prize)
    prize = wager - prize 
    plus_or_minus: int = randint(1, 2)
    if plus_or_minus == 1:
        prize = -(prize)
    print(f"Nice! You won {prize} dollars! {CASH_EMOJI}")
    wager = int(prize)
    return wager


def low(bet: int) -> int:
    """This is the slot machine's low risk, low potential reward setting."""
    global wager
    bet = int(bet)
    max_prize: int = int(wager * 1.25)
    from random import randint
    prize: int = randint(wager, max_prize)
    prize = wager - prize 
    plus_or_minus: int = randint(1, 2)
    if plus_or_minus == 1:
        prize = -(prize)
    print(f"Nice! You won {prize} dollars! {CASH_EMOJI}")
    wager = int(prize)
    return wager


def main() -> None:
    """Program entrypoint."""
    greet()
    global points
    global wager
    global player
    points = 0
    money: int = int(input("So, tell me how much money you have available! \nA reasonable investment would be anything less than $500. Give us an integer amount: "))
    if int(money) <= 0:
        print("Dang, you're really broke aren't you. Here's ten dollars.")
        points = 10
    if int(money) > 0 and int(money) <= 50:
        print("Alright, we can work with that.")
        points = money
    if int(money) > 50 and int(money) <= 100:
        print("A solid investment, I'd say.")
        points = money
    if int(money) > 100 and int(money) <= 500:
        print("Woa, are you sure you're broke?")
        points = money
    if int(money) > 500:
        print("Now let's not get too ambitious. I'll take $500 of that to wager")
        points = 500
        points = money
    continue_or_not: str = input("Print 'c' if you like to continue and risk it for the biscuit! Type anything else to exit. ")
    if continue_or_not != "c":
        if points == 1:
            print("You have one point.")
        else:
            print(f"You have {points} points.")
        print(f"I'm sorry to see you go, {player}, come back soon!")
        return None
    chat()
    print(f"You currently have {points} points! time to go get some more! \n")
    slot_machine(points)
    points = int(wager + points)
    play_again: str = input(f"Dope! You've got {points} dollars! \nType 'yes' if you'd like to play again. Type anytthing else to leave with your balance! ")
    while play_again == "yes" and points > 0:
        slot_machine(points)
        points = int(wager + points)
        if points < 0:
            print("Oopsie! It looks like you lost all your money! You can't continue with your balance, but don't worry, you can just play the game again!")
            print(f"However, it appears that you owe us {-points} dollars! You'll have to pay that back.")
            return None
        play_again = input(f"Your current balance is {points} dollars. Type 'yes' to try again! Otherwise, type 'no'. ")
    if play_again != "yes" or points < 0:
        print(f"Great job! You are leaving with {points} dollars! {FLYING_CASH} I hope to see you again soon!")
    return None


if __name__ == "__main__":
    main()
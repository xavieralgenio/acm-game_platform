def get_info():
    return {
        "name": "Wordle",
        "description": "Guess the hidden word in limited tries."
    }


def run():
    print("\nWORDLE GAME (simple version)")
    word = "code"
    tries = 3

    while tries > 0:
        guess = input("Guess word: ")

        if guess == word:
            print("You win!")
            return

        tries -= 1
        print(f"Wrong! {tries} tries left")

    print("Game Over!")
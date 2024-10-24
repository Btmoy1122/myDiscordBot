from random import choice, randint


def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if not lowered:
        return "Well you're awfully silent..."
    elif "hello" in lowered:
        return "Greetings!"
    elif "bye" in lowered:
        return "Later"
    elif "roll" in lowered:
        return f"You rolled a {randint(1, 6)}"
    elif "flip" in lowered and "coin" in lowered:
        return choice(["Heads", "Tails"])
    elif "play again" in lowered:
        return choice(["Yes", "No"])
    elif "rock" in lowered or "paper" in lowered or "scissor" in lowered:
        return choice(["Rock", "Paper", "Scissor"])
    else:
        return choice(["What??",
                       "I don't understand",
                       "I don't know",
                       "Are you talking to me?"
                       ])

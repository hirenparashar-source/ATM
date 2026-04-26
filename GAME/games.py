

import random


# ──────────────────────────────────────────
#         STONE – PAPER – SCISSORS
# ──────────────────────────────────────────

def get_computer_choice_sps():
    return random.choice(["Stone", "Paper", "Scissors"])


def decide_winner_sps(user, computer):
    if user == computer:
        return "Draw"
    wins_against = {
        "Stone": "Scissors",
        "Paper": "Stone",
        "Scissors": "Paper"
    }
    if wins_against[user] == computer:
        return "User"
    return "Computer"


def play_stone_paper_scissors():
    options = {"1": "Stone", "2": "Paper", "3": "Scissors"}
    user_score = 0
    computer_score = 0

    print("\n  ===== Stone – Paper – Scissors =====")

    while True:
        print("\n  Choose your move:")
        print("  1. Stone")
        print("  2. Paper")
        print("  3. Scissors")
        print("  4. Quit Game")
        choice = input("  Enter your choice (1-4): ").strip()

        if choice == '4':
            print(f"\n  Game Over! Final Score -> You: {user_score}  |  Computer: {computer_score}")
            break

        if choice not in options:
            print("  [ERROR] Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        user_move = options[choice]
        comp_move = get_computer_choice_sps()
        winner = decide_winner_sps(user_move, comp_move)

        print(f"\n  You chose    : {user_move}")
        print(f"  Computer chose: {comp_move}")

        if winner == "Draw":
            print("  Result       : It's a Draw!")
        elif winner == "User":
            user_score += 1
            print("  Result       : You Win this round! 🎉")
        else:
            computer_score += 1
            print("  Result       : Computer Wins this round!")

        print(f"  Score -> You: {user_score}  |  Computer: {computer_score}")


# ──────────────────────────────────────────
#              DICE ROLL GAME
# ──────────────────────────────────────────

def roll_dice():
    return random.randint(1, 6)


def play_dice_roll():
    user_score = 0
    computer_score = 0
    rounds = 0

    print("\n  ===== Dice Roll Game =====")
    print("  Highest dice roll wins each round!")

    while True:
        print("\n  1. Roll Dice")
        print("  2. Quit Game")
        choice = input("  Enter your choice (1-2): ").strip()

        if choice == '2':
            print(f"\n  Game Over! Total Rounds: {rounds}")
            print(f"  Final Score -> You: {user_score}  |  Computer: {computer_score}")
            if user_score > computer_score:
                print("  Overall Winner: YOU! 🎉")
            elif computer_score > user_score:
                print("  Overall Winner: Computer!")
            else:
                print("  Overall Result: It's a Tie!")
            break

        if choice != '1':
            print("  [ERROR] Invalid choice. Enter 1 or 2.")
            continue

        user_roll = roll_dice()
        comp_roll = roll_dice()
        rounds += 1

        print(f"\n  Your Roll     : {user_roll}")
        print(f"  Computer Roll : {comp_roll}")

        if user_roll > comp_roll:
            user_score += 1
            print("  Result        : You Win this round! 🎉")
        elif comp_roll > user_roll:
            computer_score += 1
            print("  Result        : Computer Wins this round!")
        else:
            print("  Result        : It's a Tie this round!")

        print(f"  Score -> You: {user_score}  |  Computer: {computer_score}")

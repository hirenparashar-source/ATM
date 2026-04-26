
import games  


def main():
    print("\n  ==============================")
    print("       Welcome to Mini Games   ")
    print("  ==============================")

    while True:
        print("\n  -------- Game Menu --------")
        print("  1. Stone – Paper – Scissors")
        print("  2. Dice Roll Game")
        print("  3. Exit")
        print("  ---------------------------")
        choice = input("  Enter your choice (1-3): ").strip()

        if choice == '1':
            games.play_stone_paper_scissors()

        elif choice == '2':
            games.play_dice_roll()

        elif choice == '3':
            print("\n  Thanks for playing! See you again!\n")
            break

        else:
            print("\n  [ERROR] Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

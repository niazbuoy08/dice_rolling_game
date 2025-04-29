import random

def main():
    roll_history = []
    total_rolls = 0
    sum_counts = {}
    sides = 6  # Default number of sides per die

    print("Welcome to the Enhanced Dice Roller!")
    print("Type 'help' for available commands")

    while True:
        user_input = input("\nEnter command: ").strip().lower().split()
        if not user_input:
            continue

        command = user_input[0]
        args = user_input[1:]

        if command in ['roll', 'r']:
            # Handle dice rolling
            num_dice = 2  # Default number of dice
            if args:
                try:
                    num_dice = int(args[0])
                    if num_dice < 1:
                        print("Number of dice must be at least 1. Using 2.")
                        num_dice = 2
                except ValueError:
                    print("Invalid number format. Rolling 2 dice.")
                    num_dice = 2

            # Generate rolls
            dice = [random.randint(1, sides) for _ in range(num_dice)]
            total = sum(dice)
            special = ""

            # Check for special combinations
            if num_dice == 2:
                d1, d2 = dice
                if d1 == 1 and d2 == 1:
                    special = "Snake eyes!"
                elif d1 == 6 and d2 == 6:
                    special = "Boxcars!"
                elif d1 == d2:
                    special = "Doubles!"
            else:
                if all(x == dice[0] for x in dice):
                    special = f"All {dice[0]}s!"

            # Update statistics and history
            roll_entry = (dice.copy(), total, special)
            roll_history.append(roll_entry)
            total_rolls += 1
            sum_counts[total] = sum_counts.get(total, 0) + 1

            # Display results
            print(f"Rolled: {dice}")
            print(f"Total: {total}")
            if special:
                print(f"Special: {special}")

        elif command in ['history', 'h']:
            # Display roll history
            if not roll_history:
                print("No rolls in history yet!")
            else:
                print("\nRoll History:")
                for idx, (dice, total, special) in enumerate(roll_history, 1):
                    print(f"{idx}. {dice} (Total: {total}) {special}")

        elif command in ['stats', 's']:
            # Show statistics
            print("\nStatistics:")
            print(f"Total rolls made: {total_rolls}")
            print(f"Number of sides per die: {sides}")

            if sum_counts:
                print("\nSum Statistics:")
                min_sum = min(sum_counts.keys())
                max_sum = max(sum_counts.keys())
                avg_sum = sum(k*v for k, v in sum_counts.items()) / total_rolls

                print(f"Minimum sum rolled: {min_sum}")
                print(f"Maximum sum rolled: {max_sum}")
                print(f"Average sum: {avg_sum:.2f}")

                print("\nSum Frequency:")
                for s in sorted(sum_counts):
                    print(f"Sum {s}: {sum_counts[s]} times")

        elif command in ['sides']:
            # Change number of sides
            if not args:
                print(f"Current number of sides: {sides}")
                continue

            try:
                new_sides = int(args[0])
                if new_sides < 2:
                    print("Sides must be at least 2")
                else:
                    sides = new_sides
                    print(f"Dice now have {sides} sides!")
            except ValueError:
                print("Invalid number format. Use integer values.")

        elif command in ['help', '?']:
            # Display help menu
            print("\nAvailable Commands:")
            print("roll [n] or r [n] - Roll n dice (default 2)")
            print("history or h       - Show roll history")
            print("stats or s         - Show statistics")
            print("sides [n]         - Change number of die sides")
            print("help or ?          - Show this help menu")
            print("quit or q          - Exit the program")

        elif command in ['quit', 'q', 'n']:
            # Exit program
            print("Thanks for playing!")
            break

        else:
            print("Invalid command. Type 'help' for available commands.")

if __name__ == "__main__":
    main()
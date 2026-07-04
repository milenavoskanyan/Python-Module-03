import random


PLAYERS = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "gregory",
    "John",
    "kevin",
    "Liam",
    "sophia"
]


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    print(f"Initial list of players: {PLAYERS}")

    all_upper = [player.capitalize() for player in PLAYERS]
    print(f"New list with all names capitalized: {all_upper}")

    only_upper = [player for player in PLAYERS if player[0].isupper()]
    print(f"New list of capitalized names only: {only_upper}")

    score_dict = {player: random.randint(1, 1000) for player in all_upper}
    print(f"Score dict: {score_dict}")

    score_avg = sum(score_dict[player]
                    for player in score_dict) / len(score_dict)
    print(f"Score average is {round(score_avg, 2)}")

    high_scores = {player: score_dict[player] for player in score_dict
                   if score_dict[player] > score_avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

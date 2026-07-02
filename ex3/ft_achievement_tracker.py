# len(), print(), import random, random.*, set(), set.union(),
# set.intersection(), set.difference()

import random
ACHIEVEMENTS = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder",
    ]


def gen_player_achievements() -> set:
    count = random.randint(1, len(ACHIEVEMENTS))
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()

    union = alice | bob | dylan | charlie
    print(f"All distinct achievements: {union}\n")

    intersection = dylan & bob & charlie & alice
    print(f"Common achievements: {intersection}\n")

    print(f"Only Alice has: {alice - (bob | charlie | dylan)}")
    print(f"Only Bob has: {bob - (alice | charlie | dylan)}")
    print(f"Only Charlie has: {charlie - (alice | bob | dylan)}")
    print(f"Only Dylan has: {dylan - (alice | bob | charlie)}\n")

    print(f"Alice is missing: {set(ACHIEVEMENTS) - alice}")
    print(f"Bob is missing: {set(ACHIEVEMENTS) - bob}")
    print(f"Charlie is missing: {set(ACHIEVEMENTS) - charlie}")
    print(f"Dylan is missing: {set(ACHIEVEMENTS) - dylan}")


if __name__ == "__main__":
    main()

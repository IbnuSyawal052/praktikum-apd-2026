import random


RACES = [
    ("Human", "A balanced life with no special bonuses.", {}),
    ("Elf", "Naturally gifted in magic and learning.", {"mana": 20, "knowledge": 5}),
    ("Beastkin", "Quick and sturdy, with a knack for physical training.", {"health": 10, "strength": 5}),
    ("Orc", "Powerful and tough, though less naturally magical.", {"health": 20, "strength": 10, "mana": -10}),
    ("Dragon", "A mighty heritage rich in health and mana.", {"health": 15, "mana": 25, "strength": 5}),
    ("Dwarf", "Hardy folk known for their craft and good fortune.", {"health": 10, "gold": 10}),
]

TRAITS = [
    ("Mana blessed", "Your mana and magical studies start stronger.", {"mana": 30, "knowledge": 5}),
    ("Cursed", "A mysterious curse weighs on your happiness.", {"health": -5, "happiness": -10}),
    ("Orphan", "Growing up alone made you resourceful.", {"gold": 10, "strength": 5}),
    ("Manaless", "You have no mana, but can still learn through alchemy.", {}),
]

STAT_LIMITS = {
    "health": (0, 100),
    "mana": (0, 100),
    "happiness": (0, 100),
    "strength": (0, 100),
    "knowledge": (0, 100),
}


def choose_menu(title, options):
    print(f"\n{title}")
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        choice = input("Choose a number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print(f"Enter a number from 1 to {len(options)}.")


def change_stat(character, stat, amount):
    if stat == "mana" and character["trait"] == "Manaless":
        character[stat] = 0
    elif stat in STAT_LIMITS:
        minimum, maximum = STAT_LIMITS[stat]
        character[stat] = max(minimum, min(maximum, character[stat] + amount))
    else:
        character[stat] = max(0, character[stat] + amount)


def show_status(character):
    print(f"\n--- Age {character['age']} ---")
    print(
        f"Health: {character['health']} | Mana: {character['mana']} | "
        f"Happiness: {character['happiness']}"
    )
    print(
        f"Strength: {character['strength']} | Knowledge: {character['knowledge']} | "
        f"Gold: {character['gold']}"
    )


def do_action(character, action):
    if action == 0:
        if character["mana"] > 0:
            change_stat(character, "mana", -5)
            change_stat(character, "knowledge", random.randint(8, 15))
            print("You study magic and discover a new idea.")
        else:
            change_stat(character, "knowledge", 5)
            change_stat(character, "gold", -2)
            print("Without mana, you study alchemy using a few supplies.")
    elif action == 1:
        change_stat(character, "strength", random.randint(6, 12))
        change_stat(character, "health", 2)
        print("You train hard and grow stronger.")
    elif action == 2:
        change_stat(character, "gold", random.randint(8, 18))
        change_stat(character, "happiness", -2)
        print("You spend the year working and earn some gold.")
    elif action == 3:
        change_stat(character, "health", random.randint(8, 16))
        change_stat(character, "happiness", random.randint(3, 8))
        change_stat(character, "mana", 3)
        print("You rest and recover.")
    elif action == 4:
        change_stat(character, "health", -random.randint(0, 15))
        change_stat(character, "strength", random.randint(1, 5))
        change_stat(character, "gold", random.randint(0, 20))
        print("You go on an adventure. It is exciting, but not without risk.")


def random_event(character):
    event, stat, amount = random.choice(
        [
            ("A local festival lifts your spirits.", "happiness", 8),
            ("A traveling healer helps you recover.", "health", 8),
            ("You find a purse on the road.", "gold", 10),
            ("A sudden storm leaves you chilled.", "health", -7),
            ("A kind neighbor shares a meal.", "health", 4),
        ]
    )
    change_stat(character, stat, amount)
    print(f"Event: {event}")


def main():
    print("=== A Little Life: Fantasy Realms ===")
    name = input("What is your character's name? ").strip() or "Nameless Hero"

    race_index = choose_menu("Choose your race:", [race[0] for race in RACES])
    race_name, race_description, race_bonuses = RACES[race_index]
    trait_index = choose_menu("Choose your trait:", [trait[0] for trait in TRAITS])
    trait_name, trait_description, trait_bonuses = TRAITS[trait_index]

    character = {
        "name": name,
        "race": race_name,
        "trait": trait_name,
        "age": 0,
        "health": 100,
        "mana": 50,
        "happiness": 60,
        "strength": 10,
        "knowledge": 10,
        "gold": 20,
    }

    for stat, amount in race_bonuses.items():
        change_stat(character, stat, amount)
    for stat, amount in trait_bonuses.items():
        change_stat(character, stat, amount)
    if trait_name == "Manaless":
        character["mana"] = 0

    print(f"\n{race_description} {trait_description}")
    print(f"{name} the {race_name} begins life with the {trait_name} trait.")

    actions = ["Study magic", "Train", "Work", "Rest", "Go on an adventure", "End the game"]
    while character["age"] < 80 and character["health"] > 0:
        show_status(character)
        action = choose_menu("What will you do this year?", actions)
        if action == 5:
            break

        do_action(character, action)
        character["age"] += 1
        random_event(character)

        if character["age"] == 18:
            print("Milestone: You have reached adulthood!")
        elif character["age"] == 60:
            print("Milestone: You are now a respected elder.")

    show_status(character)
    if character["health"] == 0:
        print(f"{name}'s life has come to an end at age {character['age']}.")
    elif character["age"] == 80:
        print(f"{name} has lived a full life and reached age 80.")
    else:
        print(f"You ended {name}'s story at age {character['age']}.")


if __name__ == "__main__":
    main()

import random


def simulate_single_clash(base_power, coin_power, coin_amount, sanity, enemy_power=None):
    """Calculate the strength of one side in a clash.

    The raw power is based on the base plus the contribution of each coin.
    Sanity reduces the usable power linearly from 45% to 100%.
    """
    raw_power = base_power + (coin_power * coin_amount)
    sanity_ratio = max(0.0, min(1.0, sanity / 100.0))
    effective_power = raw_power * (0.45 + 0.55 * sanity_ratio)

    if enemy_power is not None:
        if effective_power > enemy_power:
            result = "Win"
        elif effective_power < enemy_power:
            result = "Lose"
        else:
            result = "Draw"
    else:
        result = "No enemy power provided"

    return {
        "base_power": base_power,
        "coin_power": coin_power,
        "coin_amount": coin_amount,
        "sanity": sanity,
        "raw_power": raw_power,
        "effective_power": round(effective_power, 2),
        "result": result,
    }


def roll_skill_power(base_power, coin_power, coin_amount, sanity):
    """Roll a skill power where higher sanity increases the chance of success."""
    heads_chance = (50 + sanity) / 100
    heads = 0

    for _ in range(coin_amount):
        if random.random() < heads_chance:
            heads += 1

    return base_power + coin_power * heads


def simulate_clash(player, enemy, trials=10000):
    """Run repeated clash simulations and return win/lose/draw statistics."""
    results = {"win": 0, "lose": 0, "draw": 0}

    for _ in range(trials):
        player_coins = player["coin_amount"]
        enemy_coins = enemy["coin_amount"]

        while player_coins > 0 and enemy_coins > 0:
            player_power = roll_skill_power(
                player["base_power"],
                player["coin_power"],
                player_coins,
                player["sanity"],
            )
            enemy_power = roll_skill_power(
                enemy["base_power"],
                enemy["coin_power"],
                enemy_coins,
                enemy["sanity"],
            )

            if player_power > enemy_power:
                enemy_coins -= 1
            elif player_power < enemy_power:
                player_coins -= 1
            else:
                player_coins -= 1
                enemy_coins -= 1

        if player_coins > 0 and enemy_coins == 0:
            results["win"] += 1
        elif enemy_coins > 0 and player_coins == 0:
            results["lose"] += 1
        else:
            results["draw"] += 1

    return results


def read_skill(name):
    print(f"\n{name} skill")
    base_power = int(input("Base power: "))
    coin_power = int(input("Coin power: "))
    coin_amount = int(input("Number of coins: "))
    sanity = int(input("Sanity (-45 to 45): "))

    if coin_amount < 1:
        raise ValueError("A skill must have at least one coin.")
    if not -45 <= sanity <= 45:
        raise ValueError("Sanity must be between -45 and 45.")

    return {
        "base_power": base_power,
        "coin_power": coin_power,
        "coin_amount": coin_amount,
        "sanity": sanity,
    }


def main():
    print("===========================================")
    print("             CLASH SIMULATOR               ")
    print("===========================================")

    player_name = input("Player name: ").strip() or "Player 1"
    enemy_name = input("Enemy name: ").strip() or "Enemy"

    player_skill = read_skill(player_name)
    enemy_skill = read_skill(enemy_name)

    print("\nSingle clash preview:")
    player_single = simulate_single_clash(
        player_skill["base_power"],
        player_skill["coin_power"],
        player_skill["coin_amount"],
        player_skill["sanity"],
        enemy_skill["base_power"] + enemy_skill["coin_power"] * enemy_skill["coin_amount"],
    )
    print(player_single)

    clash_results = simulate_clash(player_skill, enemy_skill, trials=5000)

    print("\nEstimated clash results (5,000 simulations):")
    total = sum(clash_results.values())
    for result, count in clash_results.items():
        percentage = (count / total) * 100 if total else 0
        print(f"{result.title():<5} : {count:>4} ({percentage:.2f}%)")

    if clash_results["win"] > clash_results["lose"]:
        verdict = "Player has a better chance to win."
    elif clash_results["lose"] > clash_results["win"]:
        verdict = "Enemy has a better chance to win."
    else:
        verdict = "The clash is very balanced."

    print(f"\nVerdict: {verdict}")


if __name__ == "__main__":
    main()

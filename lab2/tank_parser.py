from pyswip import Prolog
import re

# Инициализация Prolog
prolog = Prolog()
prolog.consult("knowledge_base.pl")  # Загрузка базы знаний


def start():
    print("Hi! I will help you to choose a tank in diep.io")
    print("Please, tell me about your preferences :D")
    age_group = ask_age()
    play_style = ask_play_style()
    stats_preferences = ask_preferred_stats()
    recommended_tanks = find_tanks(play_style, stats_preferences)
    present_recommendations(recommended_tanks)


def ask_age():
    age_input = input("How old are you? ")
    try:
        try:
            age = int(age_input)
        except ValueError:
            raise ValueError(
                "  use your brain maybe? type normal (natural) numbers pls"
            )

        if age < 0 or age > 122:
            raise ValueError(
                "  what are you, Sherlok? Pentester? \n  either way i don't like you, kill yourself"
            )
        elif age == 0:
            raise ValueError("  you can't be 0 year old bruh")
        if age < 18:
            return "youth"
        elif age > 0:
            return "adult"
    except ValueError as e:
        print(str(e))
        return ask_age()


def ask_play_style():
    play_style_input = input(
        "What is your game style? (aggressive(a)/defensive(d)/balanced(b)) "
    )
    lower_input = play_style_input.lower()
    if lower_input in ["aggressive", "a"]:
        return "aggressive"
    elif lower_input in ["defensive", "d"]:
        return "defensive"
    elif lower_input in ["balanced", "b"]:
        return "balanced"
    elif lower_input == "":
        print("  Is your keyboard broken? Then type something you idiot")
        ask_play_style()
    else:
        print("  There is no style like this you dork")
        ask_play_style()


def ask_preferred_stats():
    # Define the mapping of input keys to stats
    stat_options = {
        "a": ["speed", "damage", "health"],
        "s": ["speed"],
        "d": ["damage"],
        "h": ["health"],
    }

    # Initialize an empty set to store selected stats
    selected_stats = set()

    while True:
        # Prompt the user for input
        stats_input = (
            input(
                "What stats are more important to you? \n  (speed(s), damage(d), health(h), all of them (a)) "
            )
            .strip()
            .lower()
        )

        # Check for empty input
        if not stats_input:
            print("Is your keyboard broken? Then type something you idiot.\n")
            continue  # Prompt again

        # Validate input
        if stats_input not in stat_options:
            print("Invalid input. Please enter one of the following: a, s, d, h.\n")
            continue  # Prompt again

        # Handle 'a' for all stats
        if stats_input == "a":
            selected_stats.update(stat_options["a"])
            print("You have selected all stats: Speed, Damage, Health.\n")
            break  # No need to ask further
        else:
            # Check for duplicate selection
            stat = stat_options[stats_input][0]
            if stat in selected_stats:
                print("Stop messing around dumbass.\n")
                continue  # Prompt again
            else:
                selected_stats.add(stat)
                print(f"You have selected: {stat.capitalize()}.\n")

        # Ask if the user wants to choose anything else
        while True:
            more = input("Do you want to choose anything else? (y/n): ").strip().lower()
            if more == "y":
                break  # Continue the outer loop to select more stats
            elif more == "n":
                # Check if at least one stat has been selected
                if selected_stats:
                    print(
                        f"\nYou have selected the following stats: {', '.join([stat.capitalize() for stat in selected_stats])}.\n"
                    )
                    return list(selected_stats)  # Return the selected stats as a list
                else:
                    # This case should not occur as we enforce at least one selection
                    print("You must select at least one stat.\n")
                    break  # Break to prompt again
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.\n")


def find_tanks(play_style, stats_preferences):
    # stats_prefs_prolog = '[' + ','.join(stats_preferences) + ']'
    # query = f"find_suitable_tanks({play_style}, {stats_prefs_prolog}, Tanks)"
    query = "upgrades(twin, Tanks)."
    result = list(prolog.query(query))
    print(result)
    if result:
        return [str(tank) for tank in result[0]["Tanks"]]
    else:
        return []


def suitable_for_play_style(tank, play_style):
    stats = get_tank_stats(tank)
    if not stats:
        return False
    if play_style == "aggressive":
        total_attack = stats["body_damage"] + stats["bullet_damage"] + stats["reload"]
        return total_attack >= 12 and stats["movement_speed"] >= 4
    elif play_style == "defensive":
        total_defense = (
            stats["health_regen"] + stats["max_health"] + stats["bullet_penetration"]
        )
        return total_defense >= 12
    elif play_style == "balanced":
        values = list(stats.values())
        max_stat = max(values)
        min_stat = min(values)
        diff = max_stat - min_stat
        return diff <= 2
    return False


def suitable_for_stats(tank, stats_preferences):
    stats = get_tank_stats(tank)
    if not stats:
        return False
    stats_map = {
        "скорость": stats.get("movement_speed", 0),
        "урон": stats.get("bullet_damage", 0),
        "здоровье": stats.get("max_health", 0),
    }
    for pref in stats_preferences:
        if stats_map.get(pref, 0) < 4:
            return False
    return True


def get_tank_stats(tank):
    query = f"property({tank}, stats(health_regen(HR), max_health(MH), body_damage(BD), bullet_speed(BS), bullet_penetration(BP), bullet_damage(BDam), reload(RL), movement_speed(MS){', field_of_view(FOV)' if 'field_of_view' in get_stat_names(tank) else ''}))"
    for sol in prolog.query(query):
        stats = {
            "health_regen": int(sol.get("HR", 0)),
            "max_health": int(sol.get("MH", 0)),
            "body_damage": int(sol.get("BD", 0)),
            "bullet_speed": int(sol.get("BS", 0)),
            "bullet_penetration": int(sol.get("BP", 0)),
            "bullet_damage": int(sol.get("BDam", 0)),
            "reload": int(sol.get("RL", 0)),
            "movement_speed": int(sol.get("MS", 0)),
        }
        return stats
    return None


def get_stat_names(tank):
    query = f"property({tank}, stats(Stats))"
    for sol in prolog.query(query):
        stats = sol["Stats"]
        stat_names = [stat.args[0].value for stat in stats]
        return stat_names
    return []


def present_recommendations(tanks):
    if not tanks:
        print("К сожалению, не нашлось танков, соответствующих твоим предпочтениям.")
    else:
        print("Рекомендуемые танки для тебя:")
        for tank in tanks:
            print(f"- {tank}")


if __name__ == "__main__":
    start()

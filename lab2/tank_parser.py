from pyswip import Prolog

# Инициализация Prolog
prolog = Prolog()
prolog.consult("knowledge_base.pl")  # Загрузка базы знаний


def start():
    print("Hi! I will help you to choose a tank in diep.io")
    while True:
        print("\nPlease select an option:")
        print("1. Find tanks based on your preferences")
        print("2. Find the slowest tank")
        print("3. Find the tank with highest body damage")
        print("4. Find the most balanced tank")
        print("5. Find the tank with highest overall stats")
        print("6. Find the tank with highest health to speed ratio")
        print("7. Find tanks that meet your minimum requirements")
        print("8. Find upgrade path for a tank")
        print("9. Exit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == "1":
            age_group = ask_age()
            play_styles = ask_play_style()
            stats_preferences = ask_preferred_stats()
            recommended_tanks = find_tanks(play_styles, age_group, stats_preferences)
            present_recommendations(recommended_tanks)
        elif choice == "2":
            tank = find_slowest_tank()
            print(f"The slowest tank is: {tank}")
        elif choice == "3":
            tank = find_max_body_damage_tank()
            print(f"The tank with highest body damage is: {tank}")
        elif choice == "4":
            tank = find_most_balanced_tank()
            print(f"The most balanced tank is: {tank}")
        elif choice == "5":
            tank = find_max_overall_stats_tank()
            print(f"The tank with the highest overall stats is: {tank}")
        elif choice == "6":
            tank = find_energizer_tank()
            print(f"The tank with the highest health to speed ratio is: {tank}")
        elif choice == "7":
            min_requirements = ask_min_requirements()
            tanks = find_tanks_with_min_requirements(min_requirements)
            present_recommendations(tanks)
        elif choice == "8":
            tank_name = input(
                "Enter the name of the tank to find its upgrade path: "
            ).strip()
            path = find_upgrade_path(tank_name)
            if path:
                print(f"The upgrade path for {tank_name} is: {' -> '.join(path)}")
            else:
                print(f"No upgrade path found for {tank_name}")
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


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
    # Define valid playstyle options
    playstyle_options = {"a": "aggressive", "d": "defensive", "b": "balanced"}

    selected_playstyles = set()

    while True:
        # Prompt the user for input
        play_style_input = (
            input(
                "What is your game style? \n(aggressive(a)/defensive(d)/balanced(b), you can choose multiple separated by commas) "
            )
            .strip()
            .lower()
        )

        # Check for empty input
        if not play_style_input:
            print("Is your keyboard broken? Then type something you idiot.")
            continue  # Prompt again

        # Split the input by commas and remove any extra spaces
        inputs = [s.strip() for s in play_style_input.split(",")]

        # Validate and map inputs to playstyles
        invalid_inputs = []
        for inp in inputs:
            if inp in playstyle_options:
                selected_playstyles.add(playstyle_options[inp])
            elif inp in playstyle_options.values():
                selected_playstyles.add(inp)
            else:
                invalid_inputs.append(inp)

        if invalid_inputs:
            print(f"Invalid input(s): {', '.join(invalid_inputs)}. Please try again.")
            continue  # Prompt again

        if selected_playstyles:
            print(
                f"You have selected the following play styles: {', '.join(selected_playstyles)}.\n"
            )
            return list(selected_playstyles)
        else:
            print("You must select at least one play style.")


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


def find_tanks(play_styles, game_preferences, stats_preferences):
    # Ensure play_styles is a list
    if not isinstance(play_styles, list):
        play_styles = [play_styles]

    # Convert play_styles to Prolog list format
    play_styles_prolog = "[" + ",".join(play_styles) + "]"

    # Formulate the Prolog query
    query = f"mixed_playstyles_tanks({play_styles_prolog}, TankList)"

    # Execute the query and collect results
    result = list(prolog.query(query))
    if result:
        # Extract the TankList from the result
        tank_list = result[0]["TankList"]
        # Convert Prolog atoms to strings
        tanks = [str(tank) for tank in tank_list]
        top_tanks = tanks[:5]
        return top_tanks
    else:
        return []


def suitable_for_stats(tank, stats_preferences):
    stats = get_tank_stats(tank)
    if not stats:
        return False
    stats_map = {
        "speed": stats.get("movement_speed", 0),
        "damage": stats.get("bullet_damage", 0),
        "health": stats.get("max_health", 0),
    }
    for pref in stats_preferences:
        if stats_map.get(pref, 0) < 4:
            return False
    return True


def get_tank_stats(tank):
    query = f"property({tank}, stats(health_regen(HR), max_health(MH), body_damage(BD), bullet_speed(BS), bullet_penetration(BP), bullet_damage(BDam), reload(RL), movement_speed(MS)))"
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


def present_recommendations(tanks):
    if not tanks:
        print("You better lower your standards!")
    else:
        print("Top-5 recommended tanks for you:")
        for tank in tanks:
            print(f"- {tank}")


def find_slowest_tank():
    query = "slowest(Tank)"
    result = list(prolog.query(query))
    if result:
        tank = result[0]["Tank"]
        return str(tank)
    else:
        return "No tank found."


def find_max_body_damage_tank():
    query = "max_body_damage(Tank)"
    result = list(prolog.query(query))
    if result:
        tank = result[0]["Tank"]
        return str(tank)
    else:
        return "No tank found."


def find_most_balanced_tank():
    query = "most_balanced(Tank)"
    result = list(prolog.query(query))
    if result:
        tank = result[0]["Tank"]
        return str(tank)
    else:
        return "No tank found."


def find_max_overall_stats_tank():
    query = "max_overall_stats(Tank)"
    result = list(prolog.query(query))
    if result:
        tank = result[0]["Tank"]
        return str(tank)
    else:
        return "No tank found."


def find_energizer_tank():
    query = "energizer(Tank)"
    result = list(prolog.query(query))
    if result:
        tank = result[0]["Tank"]
        return str(tank)
    else:
        return "No tank found."


def ask_min_requirements():
    while True:
        try:
            min_speed = int(input("Enter minimum movement speed (0-7): "))
            min_damage = int(input("Enter minimum bullet damage (0-7): "))
            min_reload = int(input("Enter minimum reload (0-7): "))
            if 0 <= min_speed <= 7 and 0 <= min_damage <= 7 and 0 <= min_reload <= 7:
                return {
                    "movement_speed": min_speed,
                    "bullet_damage": min_damage,
                    "reload": min_reload,
                }
            else:
                print("Values must be between 0 and 7. Please try again.")
        except ValueError:
            print("Invalid input. Please enter integer values.")


def find_tanks_with_min_requirements(min_requirements):
    ms = min_requirements["movement_speed"]
    bd = min_requirements["bullet_damage"]
    rl = min_requirements["reload"]
    query = f"find_avg_shit({ms}, {bd}, {rl}, Tank)"
    result = list(prolog.query(query))
    tanks = [str(sol["Tank"]) for sol in result]
    return tanks


def find_upgrade_path(tank_name):
    tank_name_prolog = f"'{tank_name}'"
    query = f"upgrade_path({tank_name_prolog}, Path)"
    result = list(prolog.query(query))
    if result:
        path = result[0]["Path"]
        path = [str(t) for t in path]
        return path
    else:
        return None


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
        print("You better lower your standarts bruh!")
    else:
        print("Top-5 recommended tanks for you, brother:")
        for tank in tanks:
            print(f"- {tank}")


if __name__ == "__main__":
    start()

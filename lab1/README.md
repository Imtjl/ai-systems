# Lab 1

## Part 1: Knowledge base + Prolog queries

> [!IMPORTANT]  
> I chose `diep.io` as a game. Basically, it's an online multiplayer game where
> people control toy 2d tanks of some weird geometric shapes to destroy each
> other, hence become bigger & more powerful themselves.

### Main Objects

- **Tanks**: Various types of tanks in the game.
- **Tank Classes**: Tanks divided into tiers(1-4), each representing upgrades.
- **Upgrades**: Relationships between different tanks and their corresponding
  upgrades.
- **Characteristics**: Attributes such as bullet damage, reload speed, e.t.c.
- **Abilities**: The abilities that each tank possesses.

---

### Tank Hierarchy

| ![image](./docs/hierarchy.png) |
| ------------------------------ |

There are four tiers of tanks in the game:

1. **Tier 1**: Base tanks.
2. **Tier 2**: First level of upgrades.
3. **Tier 3**: Mid-level upgrades.
4. **Tier 4**: Final upgrades with specialized abilities.

Here is the hierarchy of tanks from the image provided:

| **Tier 1** | **Tier 2**  | **Tier 3**  | **Tier 4**     |
| ---------- | ----------- | ----------- | -------------- |
| Basic Tank | Flank Guard | Auto 3      | Annihilator    |
|            | Machine Gun | Assassin    | Auto 5         |
|            | Sniper      | Destroyer   | Auto Gunner    |
|            | Twin        | Gunner      | Auto Smasher   |
|            |             | Hunter      | Auto Trapper   |
|            |             | Overseer    | Battleship     |
|            |             | Quad Tank   | Booster        |
|            |             | Smasher     | Factory        |
|            |             | Trapper     | Fighter        |
|            |             | Tri-Angle   | Glider         |
|            |             | Triple Shot | Gunner Trapper |
|            |             | Twin Flank  | Hybrid         |
|            |             |             | Landmine       |
|            |             |             | Manager        |
|            |             |             | Mega Trapper   |
|            |             |             | Necromancer    |
|            |             |             | Octo Tank      |
|            |             |             | Overlord       |
|            |             |             | Overtrapper    |
|            |             |             | Penta Shot     |
|            |             |             | Predator       |
|            |             |             | Ranger         |
|            |             |             | Rocketeer      |
|            |             |             | Skimmer        |
|            |             |             | Spike          |
|            |             |             | Sprayer        |
|            |             |             | Spread Shot    |
|            |             |             | Stalker        |
|            |             |             | Streamliner    |
|            |             |             | Tri-Trapper    |
|            |             |             | Triple Twin    |
|            |             |             | Triplet        |

---

### Properties

| ![image](./docs/stats.png) |
| -------------------------- |

Each tank has a set of properties that defines its characteristics:

| Property           | Description                                      |
| ------------------ | ------------------------------------------------ |
| Bullet Damage      | The damage that bullets deal to enemies.         |
| Bullet Penetration | The ability of bullets to pass through objects.  |
| Reload Speed       | The speed at which the tank reloads its bullets. |
| Movement Speed     | The speed of the tank's movement across the map. |
| Health             | The amount of health the tank has.               |
| Bullet Speed       | The velocity at which bullets travel.            |

---

### Upgrades

Tanks follow a structured upgrade path:

![image](./docs/upgrades.png)

---

### Now, after implementing knowledge base, let's implement queries for it


#### 1. **Simple Queries to Search for Facts**

```prolog
% Find all Tier 2 tanks:
?- tank(Tank), upgrade(Tank, basic).

% Check if `sniper` can be upgraded:
?- can_upgrade(sniper, UpgradedTank).

% Get all available upgrades for the `machine_gun` tank:
?- upgrades(machine_gun, UpgradedTanks).
```

#### 2. **Queries Using Logical Operators**

```prolog
% Find all tanks with bullet damage (bullet_damage) greater than or equal to 4 and movement speed (movement_speed) greater than or equal to 4:
?- property(Tank, stats(_, _, _, _, _, bullet_damage(BD), _, movement_speed(MS), _)), BD >= 4, MS >= 4.

% Find all tanks that do not have an upgrade:
?- tank(Tank), \+ upgrade(_, Tank).

% Find tanks with max health (max_health >= 5) or high reload speed (reload >= 5):
?- property(Tank, stats(_, max_health(MH), _, _, _, _, reload(RS), _, _)), (MH >= 5 ; RS >= 5).
```

#### 3. **Queries Using Variables to Search for Objects with Certain Characteristics**

```prolog
% Find all tanks with minimal requirements: movement speed >= 3, bullet damage >= 3, reload speed >= 3:
?- find_avg_shit(3, 3, 3, Tank).

% Find all tanks with the highest bullet speed:
?- max_bullet_speed(Tank).

% Find all tanks with the highest total sum of all stats:
?- max_overall_stats(Tank).
```

#### 4. **Queries that Require Rule Execution**

```prolog
% Find the slowest tank (with the minimum movement speed):
?- slowest(Tank).

% Find the tank with the highest health-to-speed ratio:
?- energizer(Tank).

% Get the full upgrade path for the `basic` tank:
?- upgrade_path(basic, Path).

% Find the tank with the highest body damage:
?- max_body_damage(Tank).

% Find the most balanced tank (where the difference between all stats is within 1):
?- most_balanced(Tank).
```

#### Additional Queries:

```prolog
% Check if `machine_gun` can be upgraded to `gunner`:
?- can_upgrade(machine_gun, gunner).

% Find all tanks that can be upgraded from `basic`:
?- upgrades(basic, UpgradedTanks).

% Check which tier the `sniper` tank belongs to:
?- find_tier(sniper, Tier).
```

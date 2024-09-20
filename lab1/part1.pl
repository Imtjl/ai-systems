% Tier 1 tanks
tank(basic).

% Tier 2 tanks
tank(flank_guard).
tank(machine_gun).
tank(sniper).
tank(twin).

% Tier 3 tanks
% later...



% Upgrades
upgrade(flank_guard, basic).
upgrade(machine_gun, basic).
upgrade(sniper, basic).
upgrade(twin, basic).

% More upgrades...


% Statistics
property(flank_guard, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(4), bullet_damage(4), reload(4), movement_speed(4))).
property(machine_gun, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(4), bullet_damage(3), reload(5), movement_speed(4), bullet_accuracy(2))).


% Rules

% With cut
slowest(Tank) :-
    property(Tank, stats(_, _, _, _, _, _, _, movement_speed(Min), _)),
    \+ (property(_, stats(_, _, _, _, _, _, _, movement_speed(Other), _)), Other < Min),
    !.

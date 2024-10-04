% Tier 1 tanks
tank(basic).

% Tier 2 tanks
tank(flank_guard).
tank(machine_gun).
tank(sniper).
tank(twin).

% Tier 3 tanks
tank(auto_3).
tank(assassin).
tank(destroyer).
tank(gunner).
tank(hunter).
tank(overseer).
tank(quad_tank).
tank(smasher).
tank(trapper).
tank(triangle).
tank(triple_shot).
tank(twin_flank).

% Tier 4 tanks
tank(annihilator).
tank(auto_5).
tank(auto_gunner).
tank(auto_smasher).
tank(auto_trapper).
tank(battleship).
tank(booster).
tank(factory).
tank(fighter).
tank(glider).
tank(gunner_trapper).
tank(hybrid).
tank(landmine).
tank(manager).
tank(mega_trapper).
tank(necromancer).
tank(octo_tank).
tank(overlord).
tank(overtrapper).
tank(penta_shot).
tank(predator).
tank(ranger).
tank(rocketeer).
tank(skimmer).
tank(spike).
tank(sprayer).
tank(spread_shot).
tank(stalker).
tank(streamliner).
tank(tri_trapper).
tank(triple_twin).
tank(triplet).



% Upgrades

% Tier1 -> Tier2
upgrade(flank_guard, basic).
upgrade(machine_gun, basic).
upgrade(sniper, basic).
upgrade(twin, basic).

% Tier2 -> Tier3
upgrade(auto_3, twin).
upgrade(assassin, sniper).
upgrade(destroyer, machine_gun).
upgrade(gunner, twin).
upgrade(hunter, sniper).
upgrade(overseer, sniper).
upgrade(quad_tank, twin).
upgrade(smasher, basic).
upgrade(trapper, machine_gun).
upgrade(triangle, twin).
upgrade(triple_shot, twin).
upgrade(twin_flank, twin).

% Tier3 -> Tier4
upgrade(annihilator, destroyer).
upgrade(auto_5, auto_3).
upgrade(auto_gunner, auto_3).
upgrade(auto_smasher, smasher).
upgrade(auto_trapper, trapper).
upgrade(battleship, overseer).
upgrade(booster, flank_guard).
upgrade(factory, overseer).
upgrade(fighter, overseer).
upgrade(glider, trapper).
upgrade(gunner_trapper, trapper).
upgrade(hybrid, overseer).
upgrade(landmine, trapper).
upgrade(manager, overseer).
upgrade(mega_trapper, trapper).
upgrade(necromancer, overseer).
upgrade(octo_tank, quad_tank).
upgrade(overlord, overseer).
upgrade(overtrapper, overseer).
upgrade(penta_shot, quad_tank).
upgrade(predator, hunter).
upgrade(ranger, sniper).
upgrade(rocketeer, machine_gun).
upgrade(skimmer, auto_5).
upgrade(spike, smasher).
upgrade(sprayer, triple_shot).
upgrade(spread_shot, triple_shot).
upgrade(stalker, hunter).
upgrade(streamliner, auto_gunner).
upgrade(tri_trapper, trapper).
upgrade(triple_twin, triple_shot).
upgrade(triplet, twin_flank).


% More upgrades...


% Statistics
property(flank_guard, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(4), bullet_damage(4), reload(4), movement_speed(4))).
property(machine_gun, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(4), bullet_damage(3), reload(5), movement_speed(4), bullet_accuracy(2))).
property(sniper, stats(health_regen(2), max_health(2), body_damage(2), bullet_speed(5), bullet_penetration(5), bullet_damage(4), reload(1), movement_speed(3), field_of_view(6))).
property(twin, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(3), bullet_penetration(3), bullet_damage(3), reload(4), movement_speed(4), field_of_view(3))).

% Tier 3 tanks
property(auto_3, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(3), bullet_damage(3), reload(4), movement_speed(4), field_of_view(3))).
property(assassin, stats(health_regen(2), max_health(2), body_damage(2), bullet_speed(6), bullet_penetration(6), bullet_damage(5), reload(2), movement_speed(3), field_of_view(7))).
property(destroyer, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(2), bullet_penetration(6), bullet_damage(7), reload(1), movement_speed(4), field_of_view(2))).
property(gunner, stats(health_regen(4), max_health(4), body_damage(3), bullet_speed(4), bullet_penetration(3), bullet_damage(3), reload(6), movement_speed(4), field_of_view(3))).
property(hunter, stats(health_regen(3), max_health(3), body_damage(3), bullet_speed(5), bullet_penetration(5), bullet_damage(4), reload(3), movement_speed(4), field_of_view(4))).
property(overseer, stats(health_regen(4), max_health(4), body_damage(2), bullet_speed(4), bullet_penetration(4), bullet_damage(3), reload(3), movement_speed(3), field_of_view(4))).
property(quad_tank, stats(health_regen(5), max_health(5), body_damage(5), bullet_speed(3), bullet_penetration(4), bullet_damage(3), reload(4), movement_speed(3), field_of_view(3))).
property(smasher, stats(health_regen(6), max_health(6), body_damage(6), bullet_speed(0), bullet_penetration(0), bullet_damage(0), reload(0), movement_speed(5), field_of_view(1))).
property(trapper, stats(health_regen(4), max_health(4), body_damage(3), bullet_speed(3), bullet_penetration(4), bullet_damage(3), reload(4), movement_speed(4), field_of_view(4))).
property(triangle, stats(health_regen(5), max_health(5), body_damage(4), bullet_speed(3), bullet_penetration(3), bullet_damage(3), reload(4), movement_speed(6), field_of_view(3))).
property(triple_shot, stats(health_regen(4), max_health(4), body_damage(3), bullet_speed(4), bullet_penetration(3), bullet_damage(3), reload(4), movement_speed(4), field_of_view(3))).
property(twin_flank, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(3), bullet_penetration(3), bullet_damage(3), reload(4), movement_speed(4), field_of_view(3))).

% Tier 4 tanks
property(annihilator, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(4), bullet_damage(4), reload(4), movement_speed(4), field_of_view(2))).
property(auto_5, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(3), bullet_damage(3), reload(5), movement_speed(4), field_of_view(3))).
property(auto_gunner, stats(health_regen(4), max_health(4), body_damage(3), bullet_speed(4), bullet_penetration(3), bullet_damage(3), reload(6), movement_speed(4), field_of_view(3))).
property(auto_smasher, stats(health_regen(6), max_health(6), body_damage(6), bullet_speed(0), bullet_penetration(0), bullet_damage(0), reload(0), movement_speed(5), field_of_view(1))).
property(auto_trapper, stats(health_regen(4), max_health(4), body_damage(3), bullet_speed(3), bullet_penetration(4), bullet_damage(3), reload(4), movement_speed(4), field_of_view(4))).
property(battleship, stats(health_regen(4), max_health(5), body_damage(3), bullet_speed(4), bullet_penetration(4), bullet_damage(4), reload(4), movement_speed(3), field_of_view(3))).
property(booster, stats(health_regen(6), max_health(5), body_damage(5), bullet_speed(3), bullet_penetration(3), bullet_damage(3), reload(4), movement_speed(6), field_of_view(3))).
property(factory, stats(health_regen(4), max_health(4), body_damage(3), bullet_speed(3), bullet_penetration(3), bullet_damage(3), reload(4), movement_speed(3), field_of_view(3))).
property(fighter, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(3), bullet_penetration(4), bullet_damage(3), reload(4), movement_speed(5), field_of_view(3))).
property(glider, stats(health_regen(5), max_health(4), body_damage(4), bullet_speed(3), bullet_penetration(4), bullet_damage(3), reload(4), movement_speed(5), field_of_view(3))).
property(gunner_trapper, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(3), bullet_damage(3), reload(5), movement_speed(4), field_of_view(3))).
property(hybrid, stats(health_regen(4), max_health(4), body_damage(4), bullet_speed(4), bullet_penetration(4), bullet_damage(4), reload(4), movement_speed(3), field_of_view(3))).
property(landmine, stats(health_regen(5), max_health(5), body_damage(6), bullet_speed(0), bullet_penetration(0), bullet_damage(0), reload(0), movement_speed(5), field_of_view(1))).
property(manager, stats(health_regen(4), max_health(4), body_damage(3), bullet_speed(4), bullet_penetration(4), bullet_damage(4), reload(4), movement_speed(3), field_of_view(3))).
property(mega_trapper, stats(health_regen(5), max_health(5), body_damage(5), bullet_speed(3), bullet_penetration(4), bullet_damage(3), reload(4), movement_speed(4), field_of_view(4))).
property(necromancer, stats(health_regen(4), max_health(4), body_damage(2), bullet_speed(4), bullet_penetration(3), bullet_damage(3), reload(3), movement_speed(3), field_of_view(4))).
property(octo_tank, stats(health_regen(5), max_health(5), body_damage(5), bullet_speed(3), bullet_penetration(4), bullet_damage(3), reload(4), movement_speed(3), field_of_view(3))).


% Rules

% Finds a slowest tank
slowest(Tank) :-
    property(Tank, stats(_, _, _, _, _, _, _, movement_speed(Min), _)),
    \+ (property(_, stats(_, _, _, _, _, _, _, movement_speed(Other), _)), Other < Min),
    !.

% Finds a tank with highest body damage
max_body_damage(Tank) :-
    property(Tank, stats(_, _, body_damage(Min), _, _, _, _, _, _)),
    \+ (property(_, stats(_, _, body_damage(Other), _, _, _, _, _, _)), Other > Min),
    !.

% Finds a tank with stats within 1 point of each other
most_balanced(Tank) :-
    property(Tank, stats(health_regen(HealthRegen), max_health(MaxHealth), body_damage(BodyDamage), bullet_speed(BulletSpeed), bullet_penetration(BulletPenetration), bullet_damage(BulletDamage), reload(Reload), movement_speed(MovementSpeed))),
    Diff1 is abs(HealthRegen - MaxHealth),
    Diff2 is abs(MaxHealth - BodyDamage),
    Diff3 is abs(BodyDamage - BulletSpeed),
    Diff4 is abs(BulletSpeed - BulletPenetration),
    Diff5 is abs(BulletPenetration - BulletDamage),
    Diff6 is abs(BulletDamage - Reload),
    Diff7 is abs(Reload - MovementSpeed),
    Diff1 =< 1, Diff2 =< 1, Diff3 =< 1, Diff4 =< 1, Diff5 =< 1, Diff6 =< 1, Diff7 =< 1,
    !.

% Calculates a sum of all stat values, returns tank with highest sum
max_overall_stats(Tank) :-
    property(Tank, stats(health_regen(HealthRegen), max_health(MaxHealth), body_damage(BodyDamage), bullet_speed(BulletSpeed), bullet_penetration(BulletPenetration), bullet_damage(BulletDamage), reload(Reload), movement_speed(MovementSpeed))),
    Total is HealthRegen + MaxHealth + BodyDamage + BulletSpeed + BulletPenetration + BulletDamage + Reload + MovementSpeed,
    \+ (property(_, stats(health_regen(HR), max_health(MH), body_damage(BD), bullet_speed(BS), bullet_penetration(BP), bullet_damage(BDam), reload(R), movement_speed(MS))),
        SumOther is HR + MH + BD + BS + BP + BDam + R + MS, SumOther > Total),
    !.

% Calculates biggest health to speed ratio tank for fast players
energizer(Tank) :-
    property(Tank, stats(_, max_health(MaxHealth), _, _, _, _, _, movement_speed(Speed), _)),
    Ratio is MaxHealth / Speed,
    \+ (property(_, stats(_, max_health(OtherHealth), _, _, _, _, _, movement_speed(OtherSpeed), _)),
        OtherRatio is OtherHealth / OtherSpeed, OtherRatio > Ratio),
    !.

% Finds a tank with a minimum requirements from user input
find_avg_shit(RequiredMovementSpeed, RequiredBulletDamage, RequiredReload, Tank) :-
    property(Tank, stats(_, _, _, _, _, bullet_damage(BD), reload(RS), movement_speed(MS))),
    MS >= RequiredMovementSpeed,
    BD >= RequiredBulletDamage,
    RS >= RequiredReload.

% Check if a tank can be upgraded to another
can_upgrade(Tank, NextTierTank) :-
    upgrade(NextTierTank, Tank).

% Return list of tanks that the given tank can be upgraded to
upgrades(Tank, NextTierTanks) :-
    findall(NextTierTank, upgrade(NextTierTank, Tank), NextTierTanks).

% Rule to find the full upgrade path for a tank
upgrade_path(StartTank, Path) :-
    upgrade_path_recursive(StartTank, [StartTank], Path).

% Recursive helper rule to accumulate the upgrade path
upgrade_path_recursive(Tank, Acc, Path) :-
    upgrade(NextTank, Tank),        % Find an upgrade for the current tank
    \+ member(NextTank, Acc),       % Ensure we haven't already added this upgrade to the path
    upgrade_path_recursive(NextTank, [NextTank|Acc], Path).  % Continue finding upgrades

upgrade_path_recursive(Tank, Acc, Path) :-
    \+ upgrade(_, Tank),            % Base case: no more upgrades available
    reverse(Acc, Path).             % Reverse the accumulated list to get the correct path

suitable_for_play_style(TankList, aggressive) :-
    findall(TotalAttack-Speed-T, (
        property(T, stats(_, _, body_damage(BodyDamage), _, _, bullet_damage(BulletDamage), reload(Reload), movement_speed(Speed), _)),
        TotalAttack is BodyDamage + BulletDamage + Reload,
        Speed >= 4
    ), AttackList),
    sort(0, @>=, AttackList, SortedAttackList),
    findall(Tank, member(_-_-Tank, SortedAttackList), TankList).

suitable_for_play_style(TankList, defensive) :-
    findall(TotalDefense-T, (
        property(T, stats(health_regen(HealthRegen), max_health(MaxHealth), _, _, bullet_penetration(BulletPenetration), _, _, _, _)),
        TotalDefense is HealthRegen + MaxHealth + BulletPenetration
    ), DefenseList),
    sort(0, @>=, DefenseList, SortedDefenseList),
    findall(Tank, member(_-Tank, SortedDefenseList), TankList).

suitable_for_play_style(TankList, balanced) :-
    findall(Diff-Tank, (
        property(Tank, stats(
            health_regen(HealthRegen),
            max_health(MaxHealth),
            body_damage(BodyDamage),
            bullet_speed(BulletSpeed),
            bullet_penetration(BulletPenetration),
            bullet_damage(BulletDamage),
            reload(Reload),
            movement_speed(MovementSpeed)
            % Include field_of_view(_) if necessary
        )),
        Stats = [HealthRegen, MaxHealth, BodyDamage, BulletSpeed, BulletPenetration, BulletDamage, Reload, MovementSpeed],
        max_list(Stats, MaxStat),
        min_list(Stats, MinStat),
        Diff is MaxStat - MinStat
    ), BalancedList),
    keysort(BalancedList, SortedBalancedList),
    pairs_values(SortedBalancedList, TankList).

% Collects the best tanks based on multiple playstyles
mixed_playstyles_tanks(PlayStyles, TankList) :-
    findall(Tank, tank(Tank), AllTanks),
    find_tank_scores(AllTanks, PlayStyles, TankScores),
    sort(0, @>=, TankScores, SortedTankScores),
    findall(Tank, member(_-Tank, SortedTankScores), TankList).

% Calculates scores for each tank based on playstyles
find_tank_scores([], _, []).

find_tank_scores([Tank|RestTanks], PlayStyles, [Score-Tank|RestScores]) :-
    compute_tank_score(Tank, PlayStyles, Score),
    find_tank_scores(RestTanks, PlayStyles, RestScores).

% Computes the score of a tank based on its rank in each playstyle
compute_tank_score(Tank, PlayStyles, TotalScore) :-
    findall(SingleScore, (
        member(PlayStyle, PlayStyles),
        get_tank_rank_in_playstyle(Tank, PlayStyle, Rank),
        % Invert rank to score: higher rank (lower number) gets higher score
        SingleScore is 1 / Rank
    ), Scores),
    sum_list(Scores, TotalScore).

% Retrieves the rank of a tank in a given playstyle
get_tank_rank_in_playstyle(Tank, PlayStyle, Rank) :-
    suitable_for_play_style(TankList, PlayStyle),
    (   nth1(Rank, TankList, Tank)
    ->  true
    ;   length(TankList, Length),
        Rank is Length + 1  % Assign lowest priority if tank is not in the list
    ).

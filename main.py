import random

ball = 0
counter = 0
overs = 0
runs = 0
wickets = 0
over_number = 0
overs_bowled = 0
balls_bowled = 0
runs_in_over = 0

# initialise batter variables
batter_rare = 0
batter_bye = 0
batter_legbye = 0
batter_out_stumped = 0
batter_out_lbw = 0
batter_out_caught = 0
batter_dot_ball = 0
batter_single = 0
batter_two = 0
batter_three = 0
batter_boundary = 0
batter_six = 0
total_batter_runs = 0
total_batter_wickets = 0

# initialise pitcher variables
bowler_rare = 0
bowler_wide = 0
bowler_noball = 0
bowler_out_bowled = 0
bowler_out_caught = 0
bowler_out_caught_behind = 0
bowler_dot_ball = 0
bowler_single = 0
bowler_two = 0
bowler_three = 0
bowler_boundary = 0
total_bowler_runs = 0
total_bowler_wickets = 0

# initialise location variables
cover_drive_count = 0
fine_leg_count = 0
third_man_count = 0
square_leg_count = 0
midwicket_count = 0
mid_off_count = 0
mid_on_count = 0
point_count = 0

# calculate strike rate of a batsman
def strikerate(bowls, totalruns):

    z = (float(totalruns) / bowls) * 100
    return z

# calculate bowling average
def bowling_average(runs_conceded, wickets_taken):
    if wickets_taken == 0:
        y = 0
    else:
        y = (float(runs_conceded) / wickets_taken)
    return y

def economy_rate(runs_conceded, overs_bowled):
    if balls_bowled % 6 == 0:
        x = (float(runs_conceded) / overs_bowled)
    else:
        x = (float(runs_conceded) / balls_bowled) * 6
    return x

# dice roll - entire over (120 balls)
while overs_bowled < 20:
    if wickets >= 10:
        break
    for ball in range(1, 7):
        if wickets >= 10:
            break
        dice_roll = round(random.uniform(0, 1), 3)
        balls_bowled += 1
        over_number = overs_bowled + (balls_bowled % 6) / 10
        if balls_bowled % 6 == 0:
            over_number = (overs_bowled) + 0.6
            overs_bowled += 1

# determine hit location
        def hit_location(location_dice_roll):
            if 0 <= location_dice_roll <= 236:
                hit_location = "covers"
               # increment the count for cover_drive
                global cover_drive_count
                cover_drive_count += 1
            elif 237 <= location_dice_roll <= 327:
                hit_location = "fine leg"
               # increment the count for fine_leg
                global fine_leg_count
                fine_leg_count += 1
            elif 328 <= location_dice_roll <= 421:
                hit_location = "third man"
               # increment the count for third_man
                global third_man_count
                third_man_count += 1
            elif 422 <= location_dice_roll <= 546:
                hit_location = "square leg"
               # increment the count for square_leg
                global square_leg_count
                square_leg_count += 1
            elif 547 <= location_dice_roll <= 754:
                hit_location = "midwicket"
               # increment the count for midwicket
                global midwicket_count
                midwicket_count += 1
            elif 755 <= location_dice_roll <= 831:
                hit_location = "mid-off"
                # increment the count for mid off
                global mid_off_count
                mid_off_count += 1
            elif 832 <= location_dice_roll <= 879:
                hit_location = "mid-on"
                # increment the count for mid on
                global mid_on_count
                mid_on_count += 1
            else:
                hit_location = "point"
                # increment the count for point
                global point_count
                point_count += 1
            return hit_location
        location_dice_roll = random.randint(0, 999)

    # event generator

        if 0.0 < dice_roll <= 0.001:
            batter_rare_roll = random.randint(0, 100)
            if batter_rare_roll <= 1:
                wickets += 1
                batter_rare += 1
                print(f"{over_number} - {dice_roll} - Batter Retired Out")
            elif 1 < batter_rare_roll <= 2:
                wickets += 1
                batter_rare += 1
                print(f"{over_number} - {dice_roll} - Batter Retired Hurt")
            elif 2 < batter_rare_roll <= 16:
                wickets += 1
                batter_rare += 1
                print(f"{over_number} - {dice_roll} - Batter Out - Hit Wicket")
            elif 16 < batter_rare_roll <= 17:
                wickets += 1
                batter_rare += 1
                print(f"{over_number} - {dice_roll} - Batter Out - Obstructing the Field")
            elif 17 < batter_rare_roll <= 18:
                runs += 5
                batter_rare += 1
                print(f"{over_number} - {dice_roll} - Penalty on bowling team - 5 runs")
            elif 18 < batter_rare_roll <= 33:
                runs += 4
                total_batter_runs += 4
                batter_rare += 1
                print(f"{over_number} - {dice_roll} - Non Boundary 4 runs")
            elif 33 < batter_rare_roll <= 39:
                runs += 6
                total_batter_runs += 6
                batter_rare += 1
                print(f"{over_number} - {dice_roll} - Non Boundary 6 runs")
            elif 39 < batter_rare_roll <= 100:
                runs += 5
                total_batter_runs += 5
                batter_rare += 1
                print(f"{over_number} - {dice_roll} - Batter rare - 5 runs")
        elif 0.001 < dice_roll <= 0.003:
            bye_roll = random.randint(0, 100)
            if bye_roll <= 67:
                batter_bye += 1
                runs += 1
                total_batter_runs += 1
                runs_in_over += 1
                print(f"{over_number} - {dice_roll} - Bye - 1 Run")
            elif 67 < bye_roll <= 73:
                batter_bye += 1
                runs += 2
                total_batter_runs += 2
                runs_in_over += 2
                print(f"{over_number} - {dice_roll} - Bye - 2 Runs")
            elif 73 < bye_roll <= 74:
                batter_bye += 1
                runs += 3
                total_batter_runs += 3
                runs_in_over += 3
                print(f"{over_number} - {dice_roll} - Bye - 3 Runs")
            elif 74 < bye_roll <= 99:
                batter_bye += 1
                runs += 4
                total_batter_runs += 4
                runs_in_over += 4
                print(f"{over_number} - {dice_roll} - Bye - 4 Runs")
            else:
                batter_bye += 1
                runs += 5
                total_batter_runs += 5
                runs_in_over += 5
                print(f"{over_number} - {dice_roll} - Bye - 5 Runs")
        elif 0.003 < dice_roll <= 0.018:
            legbye_roll = random.randint(0, 100)
            if legbye_roll <= 87:
                batter_legbye += 1
                runs += 1
                total_batter_runs += 1
                runs_in_over += 1
                print(f"{over_number} - {dice_roll} - Legbye - 1 Run")
            elif 87 < legbye_roll <= 92:
                batter_legbye += 1
                runs += 2
                total_batter_runs += 2
                runs_in_over += 2
                print(f"{over_number} - {dice_roll} - Legbye - 2 Runs")
            elif 92 < legbye_roll <= 93:
                batter_legbye += 1
                runs += 3
                total_batter_runs += 3
                runs_in_over += 3
                print(f"{over_number} - {dice_roll} - Legbye - 3 Runs")
            elif 93 < legbye_roll <= 99:
                batter_legbye += 1
                runs += 4
                total_batter_runs += 4
                runs_in_over += 4
                print(f"{over_number} - {dice_roll} - Legbye - 4 Runs")
            else:
                batter_legbye += 1
                runs += 5
                total_batter_runs += 5
                runs_in_over += 5
                print(f"{over_number} - {dice_roll} - Legbye - 5 Runs")
        elif 0.018 < dice_roll <= 0.020:
            batter_out_stumped += 1
            wickets += 1
            total_batter_wickets += 1
            print(f"{over_number} - {dice_roll} - Out stumped")
        elif 0.020 < dice_roll <= 0.023:
            batter_out_lbw += 1
            wickets += 1
            total_batter_wickets += 1
            print(f"{over_number} - {dice_roll} - LBW")
        elif 0.023 < dice_roll <= 0.038:
            batter_out_caught += 1
            wickets += 1
            total_batter_wickets += 1
            print(f"{over_number} - {dice_roll} - Out caught at {hit_location(location_dice_roll)}.")
        elif 0.038 < dice_roll <= 0.186:
            batter_dot_ball += 1
            print(f"{over_number} - {dice_roll} - Dot ball to {hit_location(location_dice_roll)}.")
        elif 0.186 < dice_roll <= 0.367:
            batter_single += 1
            runs += 1
            total_batter_runs += 1
            runs_in_over += 1
            print(f"{over_number} - {dice_roll} - Single to {hit_location(location_dice_roll)}.")
        elif 0.367 < dice_roll <= 0.398:
            batter_two += 1
            runs += 2
            total_batter_runs += 2
            runs_in_over += 2
            print(f"{over_number} - {dice_roll} - Two runs to {hit_location(location_dice_roll)}.")
        elif 0.398 < dice_roll <= 0.400:
            batter_three += 1
            runs += 3
            total_batter_runs += 3
            runs_in_over += 3
            print(f"{over_number} - {dice_roll} - Three runs to {hit_location(location_dice_roll)}.")
        elif 0.400 < dice_roll <= 0.455:
            batter_boundary += 1
            runs += 4
            total_batter_runs += 4
            runs_in_over += 4
            print(f"{over_number} - {dice_roll} - Boundary to {hit_location(location_dice_roll)}.")
        elif 0.455 < dice_roll <= 0.499:
            batter_six += 1
            runs += 6
            total_batter_runs += 6
            runs_in_over += 6
            print(f"{over_number} - {dice_roll} - Six to {hit_location(location_dice_roll)}!")
        elif 0.500 < dice_roll <= 0.501:
            bowler_rare += 1
            print(f"{over_number} - {dice_roll} - Bowler Rare Event")
        elif 0.501 < dice_roll <= 0.532:
            wide_roll = random.randint(0, 100)
            if wide_roll <= 91:
                bowler_wide += 1
                runs += 1
                total_batter_runs += 1
                runs_in_over += 1
                print(f"{over_number} - {dice_roll} - Wide - 1 Run")
            elif 91 < wide_roll <= 95:
                bowler_wide += 1
                runs += 2
                total_batter_runs += 2
                runs_in_over += 2
                print(f"{over_number} - {dice_roll} - Wide - 2 Runs")
            elif 95 < wide_roll <= 96:
                bowler_wide += 1
                runs += 3
                total_batter_runs += 3
                runs_in_over += 3
                print(f"{over_number} - {dice_roll} - Wide - 3 Runs")
            elif 96 < wide_roll <= 97:
                bowler_wide += 1
                runs += 4
                total_batter_runs += 4
                runs_in_over += 4
                print(f"{over_number} - {dice_roll} - Wide - 4 Runs")
            else:
                bowler_wide += 1
                runs += 5
                total_batter_runs += 5
                runs_in_over += 5
                print(f"{over_number} - {dice_roll} - Wide - 5 Runs")
        elif 0.532 < dice_roll <= 0.536:
            noball_roll = random.randint(0, 100)
            if noball_roll <= 42:
                bowler_noball += 1
                print(f"{over_number} - {dice_roll} - No ball - no runs")
            elif 42 < noball_roll <= 75:
                bowler_noball += 1
                runs += 1
                total_batter_runs += 1
                runs_in_over += 1
                print(f"{over_number} - {dice_roll} - No ball - 1 Run")
            elif 75 < noball_roll <= 81:
                bowler_noball += 1
                runs += 2
                total_batter_runs += 2
                runs_in_over += 2
                print(f"{over_number} - {dice_roll} - No ball - 2 Runs")
            elif 81 < noball_roll <= 93:
                bowler_noball += 1
                runs += 4
                total_batter_runs += 4
                runs_in_over += 4
                print(f"{over_number} - {dice_roll} - No ball - 4 Runs")
            else:
                bowler_noball += 1
                runs += 6
                total_batter_runs += 6
                runs_in_over += 6
                print(f"{over_number} - {dice_roll} - No ball - 6 Runs")
        elif 0.536 < dice_roll <= 0.537:
            bowler_out_caught_behind += 1
            wickets += 1
            total_bowler_wickets += 1
            print(f"{over_number} - {dice_roll} - Out caught behind")
        elif 0.537 < dice_roll <= 0.553:
            bowler_out_caught += 1
            wickets += 1
            total_bowler_wickets += 1
            print(f"{over_number} - {dice_roll} - Out caught at {hit_location(location_dice_roll)}.")
        elif 0.553 < dice_roll <= 0.562:
            bowler_out_bowled += 1
            wickets += 1
            total_bowler_wickets += 1
            print(f"{over_number} - {dice_roll} - Out bowled")
        elif 0.562 < dice_roll <= 0.718:
            bowler_dot_ball += 1
            print(f"{over_number} - {dice_roll} - Dot ball to {hit_location(location_dice_roll)}.")
        elif 0.718 < dice_roll <= 0.908:
            bowler_single += 1
            runs += 1
            total_bowler_runs += 1
            runs_in_over += 1
            print(f"{over_number} - {dice_roll} - Single to {hit_location(location_dice_roll)}.")
        elif 0.908 < dice_roll <= 0.940:
            bowler_two += 1
            runs += 2
            total_bowler_runs += 2
            runs_in_over += 2
            print(f"{over_number} - {dice_roll} - Three runs to {hit_location(location_dice_roll)}.")
        elif 0.940 < dice_roll <= 0.942:
            bowler_three += 1
            runs += 3
            total_bowler_runs += 3
            runs_in_over += 3
            print(f"{over_number} - {dice_roll} - Two runs to {hit_location(location_dice_roll)}.")
        else:
            bowler_boundary += 1
            runs += 4
            total_bowler_runs += 4
            runs_in_over += 4
            print(f"{over_number} - {dice_roll} - Boundary to {hit_location(location_dice_roll)}.")
    overs += 1
    print(f"end of over {overs}. {runs} runs scored. {wickets} wickets taken. runs in over {runs_in_over}\n")
    runs_in_over = 0

print("\n")

print(
    f"batter rare: {batter_rare}\nbatter bye: {batter_bye}\nbatter legbye: {batter_legbye}\nbatter out stumped: {batter_out_stumped}\nbatter out lbw: {batter_out_lbw}\nbatter out caught: {batter_out_caught}\nbatter dot ball: {batter_dot_ball}\nbatter single: {batter_single}\nbatter two: {batter_two}\nbatter three: {batter_three}\nbatter boundary: {batter_boundary}\nbatter six: {batter_six}\n")

print(
    f"bowler rare: {bowler_rare}\nbowler wide: {bowler_wide}\nbowler noball: {bowler_noball}\nbowler out bowled: {bowler_out_bowled}\nbowler out caught: {bowler_out_caught}\nbowler out caught behind: {bowler_out_caught_behind}\nbowler dot ball: {batter_dot_ball}\nbowler single: {bowler_single}\nbowler two: {bowler_two}\nbowler three: {bowler_three}\nbowler boundary: {bowler_boundary}\n")

print(f"batter total: {total_batter_runs}-{total_batter_wickets}")
print(f"bowler total: {total_bowler_runs}-{total_bowler_wickets}\n")
print(f"batter strike rate: {round(strikerate(balls_bowled, runs), 2)}")
print(f"bowling average: {round(bowling_average(runs, wickets), 2)}")
print(f"economy rate: {round(economy_rate(runs, overs), 2)}\n")

print(f"{runs}-{wickets} in {balls_bowled} balls.")
print(f"Overs: {over_number} ({overs})\n")

# print the counts for each hit location
print(f"Cover drive count: {cover_drive_count}")
print(f"Fine leg count: {fine_leg_count}")
print(f"Third man count: {third_man_count}")
print(f"Square leg count: {square_leg_count}")
print(f"Midwicket count: {midwicket_count}")
print(f"Mid off count: {mid_off_count}")
print(f"Mid on count: {mid_on_count}")
print(f"Point count: {point_count}")



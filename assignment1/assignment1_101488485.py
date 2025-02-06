# Author: Penny Ahlstrom
# Assignment: #1

gym_member = "Alec Alliton"     #string
preferred_weight_kg = 20.5      #float
highest_rep = 25                #int
membership_active = True        #bool

# workout_stats dictionary - keys (string - names of friends) and values (tuple of ints - time spent on yoga, running and weight lifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (45, 15, 20),
    "Taylor": (60, 30, 45),
}
print(workout_stats)

# Calculate the total workout minutes for each friend.
# Add total_minutes and corresponding key: <friend>_Total to the dictionary
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes
print(workout_stats)
print()

# Create a list with the header values for the workout_list table
header = ["Friend", "Yoga", "Running", "Weightlifting"]

# Data type: A list that contains lists for each element - a nested list or 2D list (table)
# Include only the original dictionary keys with the value corresponding to a tuple with workout time for each individual activity
# by filtering out the keys that end with "_Total"
workout_list = [header] + [[friend] + list(workout_stats[friend]) for friend in workout_stats if not friend.endswith("_Total")]

# Print the 2D list with each category being left-justified with a padding of 10 spaces
print("Workout List")
for category in workout_list:
    print(f"{category[0]:<10} {category[1]:<10} {category[2]:<10} {category[3]:<10}")
print()

# List workout minutes for each friend for yoga and running categories
yoga_running_minutes = [(category[0], category[1], category[2]) for category in workout_list]
print("Workout List - Yoga and Running")
for category in yoga_running_minutes:
    print(f"{category[0]:<10} {category[1]:<10} {category[2]:<10}")
print()

# List workout minutes for last two friends for weightlifting category
last_two_friends = [workout_list[0]] + workout_list[-2:]
weightlifting_minutes = [(category[0], category[3]) for category in last_two_friends]
print("Workout List - Weightlifting (last two friends only)")
for category in weightlifting_minutes:
    print(f"{category[0]:<10} {category[1]:<10}")
print()

# Print a congratulatory message to any friend whose total workout time exceeds 120 minutes
for friend, total_minutes in workout_stats.items():
    # Check if the key ends with "_Total" and the total workout minutes are >= 120
    if friend.endswith("_Total") and total_minutes >= 120:
        # Get the friend's name by removing the "_Total" suffix
        friend_name = friend.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")
print()

# Print individual and total workout minutes for a friend if they exist in the dictionary
input_friend = input("Write the name of the friend you would like to see workout stats for: ").lower()
print()
for friend in workout_stats:
    if friend.lower() == input_friend:
        workout_minutes = workout_stats[friend]
        total_minutes = workout_stats.get(friend + "_Total")
        workout_time_units = "minutes"
        print(f"{friend}'s Workout Stats:")
        print(f"Yoga: {workout_minutes[0]} {workout_time_units}, Running: {workout_minutes[1]} {workout_time_units}, "
              f"Weightlifting: {workout_minutes[2]} {workout_time_units}, and Total: {total_minutes} {workout_time_units}")
        break
else:
    print(f"Friend {input_friend} not found in the records.")
print()

# Print the friend and their total workout minutes for both the highest and lowest total
friend_totals = {friend: workout_stats.get(friend + "_Total") for friend in workout_stats if not friend.endswith("_Total")}

# Find the friend with the highest total minutes
max_friend = max(friend_totals, key=friend_totals.get)
max_minutes = friend_totals[max_friend]

# Find the friend with the lowest total minutes
min_friend = min(friend_totals, key=friend_totals.get)
min_minutes = friend_totals[min_friend]

# Print the results
print(f"Friend with the highest total workout minutes: {max_friend} with {max_minutes} minutes")
print(f"Friend with the lowest total workout minutes: {min_friend} with {min_minutes} minutes")
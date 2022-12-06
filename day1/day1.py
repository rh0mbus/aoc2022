file = open('input.txt', 'r')

calories = 0
calories_per_elf = []
highest_calorie_count = -1

for line in file:
    if len(line) > 1:
        calories += int(line)
    if len(line) == 1:
        calories_per_elf.append(calories)
        calories = 0
else:
    calories_per_elf.append(calories)
    calories = 0

for elf in calories_per_elf:
    if elf > highest_calorie_count:
        highest_calorie_count = elf

calories_per_elf.sort(reverse=True)

for elf in calories_per_elf[0:3]:
    calories += elf

print(calories_per_elf[0:3])
print(highest_calorie_count)
print(calories)
file.close()
keep = input("Please enter the die you'd like to keep, separated by spaces (enter zero to reroll all): ").split()
for i in range(len(keep)):
    keep[i] = int(keep[i])
print(keep)

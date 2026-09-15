num = int(input("Enter a number: "))
tot = 0
valid = 0
while num > 0:
    tot = tot + num
    valid += 1
    print(f"Total: {tot} valid entries: {valid}")
    num = int(input("Enter a number: "))

    if tot + num == 100:
        print("You've made it to 100")
        break
    elif tot + num > 100:
        print(f"You've gone over 100 there where a total of {valid} valid entries")
        break
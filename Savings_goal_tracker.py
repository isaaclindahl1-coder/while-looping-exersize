goal = float(input("Enter your positive savings goal: "))
deposit = float(input("Enter your positive weekly deposit: "))
week = 0
balance = 0
while balance < goal:
    week += 1
    balance += deposit
    print(f"weeks: {week}  balance = ${balance: .2f}")
    deposit = float(input("Enter your possitive weekly balence: "))
    if balance >= goal:
        print("You have reached your goal!!! good job!!!")
        break
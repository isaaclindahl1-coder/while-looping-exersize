level_number = input("Enter a level number: ").strip()
rejatemps = int(0)
while level_number.isdigit() == False:
    print("invalid entry")
    level_number = input("Enter a level number: ").strip()
    rejatemps = int(rejatemps + 1)
level_number = int(level_number)
while int(level_number) < 10 or int(level_number) > 50:
    level_number = int(level_number)
    level_number = input("Enter a level number: ").strip()
    rejatemps = int(rejatemps + 1)
    while level_number.isdigit() == False:
        print("invalid entry, not a number.")
        level_number = input("Enter a level number: ").strip()
        rejatemps = int(rejatemps + 1)

print(f"It took {rejatemps} attempts to enter your level which is {level_number}.")

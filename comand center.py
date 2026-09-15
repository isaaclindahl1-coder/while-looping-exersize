import random
count = 0
while True:
    print("1. Say Hello")
    print("2. Display a Random Number 1 to 100")
    print("3. Show How Many Actions Have Been Completed")
    print("q. Quit")

    choice = input("Pick an option: ").strip().lower()
    if choice == "1":
        print("Hello")
        count =  count + 1

    elif choice == "2":
        print(random.randint(1, 100))
        count = count + 1

    elif choice == "3":
        print(count)
        count = count + 1

    elif choice == "q":
        count = count + 1
        break

    else:
        print("That is not a vaild input please try again")


    

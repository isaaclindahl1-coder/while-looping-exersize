password = "password123"
atmp = 3
enter = input(f"You have {atmp} attempts remaining - Enter password: ")

while enter != password and atmp  > 1:
    print("THAT PASSWORD IS NOT CORRECT PLEASE TRY AGAIN")
    atmp -= 1
    enter = input(f"You have {atmp} attempts remaining - Enter password: ")
if enter == password:
    print("ACCESS GRANTED")
else:
    print("ACOUNT LOCKED")

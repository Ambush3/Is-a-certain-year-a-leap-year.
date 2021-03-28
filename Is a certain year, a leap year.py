year = int(input("Which year do you want to check? "))

if year % 4 == 0:

    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}, Leap year.")

        else:
            print(f"{year}, not Leap year.")

    else:
        print(f"{year}, Leap year.")

else:

    print(f"{year}, not a Leap Year.")








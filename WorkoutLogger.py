from datetime import date, time

# With this function, i'm getting the type of activity the user has done.
while True:
    try:
        def activitymenu():
            print("""
            - Welcome to WorkoutLogger 1.0 -
            What you wanna to log today?\n
            1. Run
            2. Walk
            3. Quit
            """)
            return int(input("Choose the activity type: "))
        activity = activitymenu()
        if activity == 3:
            quit()
        elif activity > 3 or activity < 1:
            print("\nPlease, choose a number between 1 and 3.")
            continue
    except ValueError:
        print("\nPlease, choose a valid number.")
        continue
    break

# And with this one, i'm getting the type of measurement system the user prefers.
while True:
    try:
        def measurementmenu():
            print("""
            1. Imperial
            2. Metric
            3. Quit
            """)
            return int(input("Choose the measurement system: "))
        measurement = measurementmenu()
        if measurement == 3:
            quit()
        elif measurement > 3 or measurement < 1:
            print("\nPlease, choose a number between 1 and 3.")
            continue
    except ValueError:
        print("\nPlease, choose only numbers.")
        continue
    break

# With these two lines of code i'll get the person's name and the day's date.
name = str(input("Your name: "))
date = date.today()

# Here, i'll get the distance the user has inputted.
while True:
    try:
        distance = int(input("Type the distance: "))
        if distance < 1:
            print("\nPlease, use only positive number.\n")
    except ValueError:
        print("\nPlease, use only numbers.\n")
        continue
    break

# With these lines i'll output the user entries to the .txt file.
match activity:
    case 1:
        match measurement: #type: ignore
            case 1:
                with open("WorkoutLogger1.0.txt", "a") as f:
                    f.write(f"On the day {date}, {name} ran for {distance} miles.\n")
            case 2:
                with open("WorkoutLogger1.0.txt", "a") as f:
                    f.write(f"On the day {date}, {name} ran for {distance} kilometers.\n")
    case 2:
        match measurement: #type: ignore
            case 1:
                with open("WorkoutLogger1.0.txt", "a") as f:
                    f.write(f"On the day {date}, {name} walked for {distance} miles.\n")
            case 2:
                with open("WorkoutLogger1.0.txt", "a") as f:
                    f.write(f"On the day {date}, {name} walked for {distance} kilometers.\n")

print("\nThank you for using WorkoutLogger 1.0, we hope to see you again!\n")
command = ""
already_started = False
while True:
    command = input(">")
    if command == "start":
        if already_started:
            print("Car is already started")
        else:
            already_started = True
            print("the car is started")
    elif command == "stop":
        if not already_started:
            print("Car is already stopped")
        else:
            already_started = False
            print("the car has stopped")
    elif command == "help":
        print(
            "start - to start the car"
            "stop - to stop the car"
            "quit - to quit the program"
        )
    elif command == "quit":
        break
    else: print("i don't understand the command")

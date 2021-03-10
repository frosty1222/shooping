command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
        print("car started...")
    elif command == "stop":
        if not started:
            print("Car is already stoped")
        else:
            Started = False
        print("car stoped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car 
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")

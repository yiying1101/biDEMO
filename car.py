command=""
started=False
while True:
    command=input(">").lower()
    if command == "start" :
        if started:
          print("car is already started")
        else:
            started=True
            print('car is started')
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
             started =False
             print("car is stopped")
    elif command =="help" :
        print("""
start-to start the car
stop-to stop the cat
quit-to quit        """)
    elif command =="quit":
        print("叫你退出")
        break
    else:
        print("you are joker")







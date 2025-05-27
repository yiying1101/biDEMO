secret_number=10
chai_count=0
chai_limit=5
while chai_count<chai_limit:
    john=int(input("猜一猜:"))
    chai_count +=1
    if john==secret_number:
        print("you are win")
        break
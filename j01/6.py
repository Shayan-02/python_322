user1 = input("entekhab konid (sang, kaghaz, gheychi): ")
user2 = input("entekhab konid (sang, kaghaz, gheychi): ")

if user1 == "sang" or user1 == "kaghaz" or user1 == "gheychi":
    if user2 == "sang" or user2 == "kaghaz" or user2 == "gheychi":
        if user1 == user2:
            print("mosavi")
        else:
            if user1 == "sang":
                if user2 == "kaghaz":
                    print(user2)
                else:
                    print(user1)
            elif user1 == "kaghaz":
                if user2 == "gheychi":
                    print(user2)
                else:
                    print(user1)
            elif user1 == "gheychi":
                if user2 == "sang":
                    print(user2)
                else:
                    print(user1)
    else:
        print("user2 ghalateh")
else:
    print("user1 ghalateh")
